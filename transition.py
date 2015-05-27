#from variable import Variable
from side import Side
from side import SideException
from conditions import Condition
from conditions import StateConditions
from conditions import CustomConditions


class Transition(object):
    def __init__(self, left_side, right_side):
        assert isinstance(left_side, Side) and isinstance(right_side, Side)
        self.__left = left_side
        self.__right = right_side
        #test property, need to review
        self.__is_simple = False

    def __str__(self):
        return "{} ---> {}".format(str(self.__left), str(self.__right))

    def set_simple(self):
        self.__is_simple = True

    def get_simple(self):
        return self.__is_simple

    def check_triviality(self):
        return self.__left.is_trivial() and self.__right.is_trivial()

    def copy(self):
        return Transition(self.__left.copy(), self.__right.copy())

    def apply_condition(self, condition):
        condition_left = condition.get_left_side()
        condition_right = condition.get_right_side()
        if self.__left.contains(condition_left) and (
                not condition_right.contains_unknown() or
                len(condition_right) == 1):
            self.__left.replace_in_side(condition_left, condition_right)

        if self.__right.contains(condition_left):
            self.__right.replace_in_side(condition_left, condition_right)

    def has_empty_side(self):
        return self.__left.is_empty() or self.__right.is_empty()

    def has_both_empty_side(self):
        return self.__left.is_empty() and self.__right.is_empty()

    def get_left_side(self):
        return self.__left

    def get_right_side(self):
        return self.__right

    def make_condition(self):

        def get_state_for_side(side):
            if side.is_empty():
                return StateConditions.IS_ZERO
            return StateConditions.IS_EQUAL

        non_zero_side = None
        if self.__left.is_empty() and not self.__right.is_empty():
            non_zero_side = self.__right
        elif not self.__left.is_empty() and self.__right.is_empty():
            non_zero_side = self.__left
        else:
            raise Exception("Can not make condition with non zero side")
        try:
            latest_unknown = non_zero_side.find_the_latest_unknown()
            #print "latest_unknown = ", str(latest_unknown)
            non_zero_side.pop_variable(latest_unknown)
            state = get_state_for_side(non_zero_side)
            return Condition(Side(latest_unknown), non_zero_side, state)
        except SideException:
            try:
                lat_output = non_zero_side.find_the_latest_output()
                non_zero_side.pop_variable(lat_output)
                state = get_state_for_side(non_zero_side)
                return Condition(Side(lat_output), non_zero_side, state)
            except SideException:
                lat_input = non_zero_side.find_the_latest_input()
                non_zero_side.pop_variable(lat_input)
                state = get_state_for_side(non_zero_side)
                return Condition(Side(lat_input), non_zero_side, state)


class SystemTransition(object):

    def __init__(self, *transitions):
        assert all([isinstance(x, Transition) for x in transitions])
        self.__transitions = list(transitions)

    def __str__(self):
        system = ""
        for ind in xrange(len(self.__transitions)):
            system += "%d) %s\n" % (ind + 1, str(self.__transitions[ind]))
        return system

    def copy(self):
        transitions = [tr.copy() for tr in self.__transitions]
        return SystemTransition(*transitions)

    def apply_condition(self, condition):
        assert isinstance(condition, Condition)
        for transition in self.__transitions:
            transition.apply_condition(condition)

    def apply_conditions(self, conditions):
        assert isinstance(conditions, list)
        for condition in conditions:
            self.apply_condition(condition)

    def analyse_and_set_custom_conditions(self, custom_cond):
        null_trans = []
        rm = []
        for transition in self.__transitions:
            if transition.has_both_empty_side():
                #print "will rm == ", transition
                rm.append(transition)
            elif transition.has_empty_side():
                #print "emty == ", transition
                null_trans.append(transition)

        for transition in null_trans:
            self.__transitions.remove(transition)

        map(self.__transitions.remove, rm)

        for trans in null_trans:
            custom_cond.append_condition(trans.make_condition())

    def apply_custom_conditions(self, custom_conditions):
        for index in xrange(len(custom_conditions) - 1, -1, -1):
            condition = custom_conditions.get_condition(index)
            self.apply_condition(condition)

    def apply_common_condition(self, common_condition):
        zero_conds = common_condition.get_zero_condition()
        for condition in zero_conds:
            self.apply_condition(condition)

    def has_condition(self):
        return any([tr.has_empty_side() for tr in self.__transitions])

    def do_fast_estimation(self, custom_cond, common_in, common_out):
        nz_c = list(common_in.get_non_zero_condition())
        nz_c.extend(common_out.get_non_zero_condition())
        nz_sides = [cond.get_left_side() for cond in nz_c]

        count_simple = 0
        for trans in self.__transitions:
            tr_left = trans.get_left_side()
            tr_right = trans.get_right_side()

            if tr_left in nz_sides and tr_right not in nz_sides:
                custom_cond.append_condition(
                    Condition(tr_right, Side(), StateConditions.IS_NOT_ZERO))
                if tr_right.has_only_one_unknown():
                    trans.set_simple()
                    count_simple += 1
            elif tr_left not in nz_sides and tr_right in nz_sides:
                custom_cond.append_condition(
                    Condition(tr_left, Side(), StateConditions.IS_NOT_ZERO))
                if tr_left.has_only_one_unknown():
                    trans.set_simple()
                    count_simple += 1

            if not tr_left.contains_unknown() and (
                    not tr_right.contains_unknown()):
                trans.set_simple()
                count_simple += 1

        return count_simple == len(self.__transitions)
