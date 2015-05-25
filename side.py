from variable import Variable


class Side(object):
    def __init__(self, *args):
        assert all([isinstance(x, Variable) for x in args])
        self.__vars = args

    def __eq__(self, other):
        if len(self.__vars) == len(other.__vars):
            for x in xrange(len(self.__vars)):
                if self.__vars[x] != other.__vars[x]:
                    return False
            return True
        return False

    def __str__(self):
        str_vars = map(lambda var: "[" + str(var) + "]", self.__vars)
        return " XOR ".join(str_vars) if len(str_vars) > 0 else "[]"

    def equals(self, other):
        return self.__eq__(other)

    def contains(self, other):
        for var in other.__vars:
            if var not in self.__vars:
                return False
        return True

    def contains_element(self, element):
        return element in self.__vars

    def contains_unknown(self):
        return any([var.is_unknown() for var in self.__vars])

    def is_trivial(self):
        return all(map(lambda x: not x.is_unknown(), self.__vars))

    def is_empty(self):
        return len(self.__vars) == 0

    def copy_with_cond(self, conditions):
        new_vars = []
        for element in self.__vars:
            for condition in conditions:
                if condition.get_left_side().contains_element(element):
                    break
            else:
                new_vars.append(element)

        return Side(*new_vars)

    def get_vars(self):
        return self.__vars

    def find_the_latest_unknown(self):
        if not self.contains_unknown():
            raise Exception("No one unknown Variable in Side")
        max_var = None
        for var in self.__vars:
            if var.is_unknown():
                if max_var is None or var > max_var:
                    max_var = var

        assert max_var is not None
        return max_var

    def has_only_one_unknown(self):
        return len(self.__vars) == 1 and self.__vars[0].is_unknown()

    def pop_variable(self, var):
        length = len(self.__vars)
        assert self.contains_element(var)
        self.__vars.remove(var)
        assert len(self.__vars) == length - 1

    def replace_in_side(self, would_repl, replacement):
        """ all variables in 'would_repl' will be replaced to 'replacement' """
        assert isinstance(would_repl, Side) and isinstance(replacement, Side)
        assert self.contains(would_repl)
        #remove all elements from would_repl in self
        for var in would_repl.__vars:
            self.pop_variable(var)

        # add all elements from replacement to self
        for var in replacement.__vars:
            self.add_variable(var)

    def add_variable(self, variable):
        if self.contains_element(variable):
            self.pop_variable(variable)
        else:
            self.__vars.append(variable)
