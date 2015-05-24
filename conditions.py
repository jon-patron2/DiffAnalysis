from enum import Enum
from variable import Variable
from side import Side


class StateConditions(Enum):
    IS_ZERO = 0
    IS_NOT_ZERO = 1
    IS_EQUAL = 2
    IS_SUMM = 3


class Condition(object):
    """ class describe conditions for system of transitions"""
    def __init__(self, left_side, right_side, state):
        """

        left_side - is list of Variables
        left_side - is list of Variables or None if state eqaul
                        to StateConditions.IS_ZERO
        state - state of condition

        """
        super(Condition, self).__init__()
        if right_side is not None and state != StateConditions.IS_ZERO:
            raise Exception("Bad values in arguments")
        assert isinstance(left_side, Side)
        assert right_side is None or isinstance(right_side, Side)
        self.__state = state
        self.__left_side = left_side
        self.__right_side = right_side

    def __eq__(self, condition_obj):
        assert isinstance(condition_obj, Condition)
        print ("Method __eq__ of Condition is called")
        assert 1 == 0  # not implemented

    def __str__(self):
        if self.__state == StateConditions.IS_ZERO:
            return str(self.__left_side) + " = 0"
        elif self.__state == StateConditions.IS_NOT_ZERO:
            return str(self.__left_side) + " != 0"
        else:
            return str(self.__left_side) + " = " + str(self.__right_side)

    def get_left_side(self):
        return self.__left_side

    def get_state(self):
        return self.__state

    @staticmethod
    def create_from_transaction(trans):
        assert trans.has_empty_side()
        side = None
        if trans.get_left_side().is_empty():
            side = trans.get_right_side()
        else:
            side = trans.get_left_side()

        unknown_part = []
        known_part = []
        varibs = side.get_vars()
        for var in varibs:
            if var.is_unknown():
                unknown_part.append(var)
            else:
                known_part.append(var)
        return Condition(
            Side(*unknown_part), Side(*known_part), StateConditions.IS_SUMM)


class CommonConditions(object):
    """ condition for input and output variables """
    def __init__(self, *input_variables):
        assert all([isinstance(x, Variable) and x.is_input()
                    for x in input_variables])
        self.__input_variables = input_variables
        self.__conditions = []
        self.__complements = []
        self.__amount = -1

    @staticmethod
    def get_num_bits(number, max_bits):
        res = []
        counter = 0
        comp = 1
        while counter < max_bits:
            if (comp & number) > 0:
                res.append(counter)
            counter += 1
            comp *= 2
        return res

    @staticmethod
    def comparator(lst1, lst2):
        if len(lst1) < len(lst2):
            return -1
        elif len(lst1) > len(lst2):
            return 1
        else:
            return 1 if lst1 > lst2 else -1

    def generate_conditions(self):
        if len(self.__conditions) > 0:
            return self.__conditions

        max_bits = len(self.__input_variables)
        max_number = pow(2, max_bits)

        all_zero_pos = []

        for x in xrange(1, max_number - 1):
            all_zero_pos.append(self.get_num_bits(x, max_bits))
        all_zero_pos.sort(self.comparator)

        for zero_pos in all_zero_pos:
            zero_vars = []
            none_zero_vars = []
            for ind in xrange(len(self.__input_variables)):
                if ind in zero_pos:
                    zero_vars.append(Condition(
                        Side(self.__input_variables[ind]),
                        None,
                        StateConditions.IS_ZERO)
                    )
                else:
                    none_zero_vars.append(Condition(
                        Side(self.__input_variables[ind]),
                        None,
                        StateConditions.IS_NOT_ZERO))
            self.__conditions.append(zero_vars)
            self.__complements.append(none_zero_vars)
        self.__amount = len(self.__conditions)
        return "OK"

    def get_amount_conditions(self):
        return self.__amount

    def get_common_cond(self, index):
        if index > self.__amount - 1 or index < 0:
            raise Exception("Wrong index")
        return self.__conditions[index]

    def get_complem_com_cond(self, index):
        if index > self.__amount - 1 or index < 0:
            raise Exception("Wrong index")
        return self.__complements[index]


class CustomConditions(object):
    """
    conditions which is created during applying CommonConditions and assumption
    """
    def __init__(self, *conditions):
        self.__conditions = conditions

    def recalculation_conditions(self):
        for cond in self.__conditions:
            raise Exception("Not implemented")
