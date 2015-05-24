#from variable import Variable
from side import Side
from conditions import Condition
from conditions import StateConditions


class Transition(object):
    def __init__(self, left_side, right_side):
        assert isinstance(left_side, Side) and isinstance(right_side, Side)
        self.__left = left_side
        self.__right = right_side

    def __str__(self):
        return "{} ---> {}".format(str(self.__left), str(self.__right))

    def check_triviality(self):
        return self.__left.is_trivial() and self.__right.is_trivial()

    def copy_with_cond(self, condition):
        new_left = self.__left.copy_with_cond(condition)
        new_right = self.__right.copy_with_cond(condition)
        return Transition(new_left, new_right)

    def has_empty_side(self):
        return self.__left.is_empty() or self.__right.is_empty()

    def get_left_side(self):
        return self.__left

    def get_right_side(self):
        return self.__right

    def make_condition(self):
        non_zero_side = None
        if self.__left.is_empty() and not self.__right.is_empty():
            non_zero_side = self.__right
        elif not self.__left.is_empty() and self.__right.is_empty():
            non_zero_side = self.__left
        else:
            raise Exception("Can not make condition with nor zero side")

        latest_unknown = non_zero_side.find_the_latest_unknown()
        non_zero_side.pop_variable(latest_unknown)
        return Condition(
            Side(latest_unknown), non_zero_side, StateConditions.IS_EQUAL
        )


class SystemTransition(object):

    def __init__(self, *transitions):
        assert all([isinstance(x, Transition) for x in transitions])
        self.__transitions = transitions

    def __str__(self):
        system = ""
        for ind in xrange(len(self.__transitions)):
            system += "%d) %s\n" % (ind + 1, str(self.__transitions[ind]))
        return system

    def copy_with_cond(self, condition):
        """ copy system use common condition """
        new_t = [tran.copy_with_cond(condition) for tran in self.__transitions]
        return SystemTransition(*new_t)

    def analyse_and_get_custom_cond(self, complements):
        null_trans = []
        for ind in xrange(len(self.__transitions)):
            if self.__transitions.has_empty_side():
                null_trans.append(ind)
        null_trans.sort(reverse=True)
        print null_trans
        null_trans = [self.__transitions.pop(x) for x in null_trans]
        print null_trans
        custom_con = []
        for trans in null_trans:
            custom_con.append(Condition.create_from_transaction(trans))
        print " ".join(map(str, custom_con))
        return custom_con
