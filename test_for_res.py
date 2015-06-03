def contains_only_str(lst):
    return all(isinstance(elem, str) for elem in lst)


def contains_only_tuples(lst):
    return all(isinstance(elem, tuple) for elem in lst)


def contains_list(lst):
    return any(isinstance(elem, list) for elem in lst)


def remove_empty_str(lst):
    while '' in lst:
        lst.remove('')


def is_empty_fork(lst):
    return len(lst) == 1 and lst[0] == 'fork'


def is_fork_list(lst):
    # print "call is_fork_list with " + str(lst)
    if lst[0] == 'fork':
        # print "first fork"
        for x in xrange(1, len(lst)):
            if not isinstance(lst[x], tuple):
                # print "%s not tup" % str(lst[x])
                return False
        return True
    #  print "do not found fork"
    return False


def get_max_from_tuples(lst):
    assert len(lst) > 0 and contains_only_tuples(lst)
    max_val = lst[0]

    for tup in lst:
        if tup[1] > max_val[1]:
            max_val = tup

    return max_val


def get_sum(lst):
    assert not is_empty_fork(lst)
    assert lst[0] == 'fork'

    res_str = ''
    res_value = 0
    for x in xrange(1, len(lst)):
        tup = lst[x]
        res_str += " + " + tup[0]
        res_value += tup[1]

    return (res_str[3:], res_value)


def merge_fork(lst):
    remove_empty_str(lst)
    for x in xrange(len(lst)):
        if isinstance(lst[x], list):
            # print "found list " + str(lst[x])
            remove_empty_str(lst[x])
            if len(lst[x]) == 0 or is_empty_fork(lst[x]):
                lst[x] = ''
                # print "found epty " + str(lst[x])
            elif is_fork_list(lst[x]):
                # print "found fork " + str(lst[x])
                lst[x] = get_sum(lst[x])
            else:
                # print "goto rec with " + str(lst[x])
                merge_fork(lst[x])


def choose_max(lst):
    remove_empty_str(lst)
    for x in xrange(len(lst)):
        if isinstance(lst[x], list):
            remove_empty_str(lst[x])
            if contains_only_tuples(lst[x]):
                lst[x] = get_max_from_tuples(lst[x])
            else:
                choose_max(lst[x])


# test2 = [['fork', ('p^4', 1), ('p^5', 0.5)]]
# merge_fork(test2)
# print "after " + str(test2)

# exit(0)
def get_normalise_result(lst):
    while contains_list(lst):
        # print "="*50 + "new iteration" + "="*50
        choose_max(lst)
        # print "af choose_max = " + str(lst)
        merge_fork(lst)
        # print "af merge_fork = " + str(lst)
        # print "="*50 + "new iteration end" + "="*50
