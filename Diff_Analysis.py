from variable import TypeVariable
from variable import Variable
from side import Side
from transition import Transition
from transition import SystemTransition
# from conditions import Condition
from conditions import CommonConditions
from conditions import CustomConditions


def get_estimation(est_data):
    if est_data["fail"]:
        return "Fail"

    return "p^%d * p^(%d - %d) = p^%d" % (
        est_data["transition_triviality"],
        est_data["transition_with_unknowns"],
        est_data["count_unknown_vars"],
        est_data["transition_triviality"] +
        est_data["transition_with_unknowns"] - est_data["count_unknown_vars"]
    )


def print_results(results):
    for estimations in results:
        print "\n\n"
        for est in estimations:
            print get_estimation(est)


a1 = Variable(TypeVariable.INPUT)
a2 = Variable(TypeVariable.INPUT)
a3 = Variable(TypeVariable.INPUT)

g1 = Variable(TypeVariable.OUTPUT)
g2 = Variable(TypeVariable.OUTPUT)
g3 = Variable(TypeVariable.OUTPUT)

b1 = Variable(TypeVariable.UNKNOWN)
b2 = Variable(TypeVariable.UNKNOWN)
b3 = Variable(TypeVariable.UNKNOWN)
b4 = Variable(TypeVariable.UNKNOWN)
b5 = Variable(TypeVariable.UNKNOWN)
b6 = Variable(TypeVariable.UNKNOWN)
b7 = Variable(TypeVariable.UNKNOWN)
b8 = Variable(TypeVariable.UNKNOWN)


# t1 = Transition(Side(a1), Side(a2, a3, b1))
# t2 = Transition(Side(a2), Side(a3, b1, b2))
# t3 = Transition(Side(a3), Side(b1, b2, b3))
# t4 = Transition(Side(b1), Side(b2, b3, b4))
# t5 = Transition(Side(b2), Side(b3, b4, g1))
# t6 = Transition(Side(b3), Side(b4, g1, g2))
# t7 = Transition(Side(b4), Side(g1, g2, g3))


t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, b7))
t8 = Transition(Side(b5), Side(b6, b7, b8))
t9 = Transition(Side(b6), Side(b7, b8, g1))
t10 = Transition(Side(b7), Side(b8, g1, g2))
t11 = Transition(Side(b8), Side(g1, g2, g3))

system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
print "Basic system is: \n" + str(system) + "\n\n"

print "Creating common conditions..."
input_conditions = CommonConditions(a1, a2, a3)
output_conditions = CommonConditions(g1, g2, g3)

print "generating ..."
print "input conditions... " + input_conditions.generate_conditions()
print "output conditions... " + output_conditions.generate_conditions()

amount_conditions = len(input_conditions)
assert amount_conditions == len(output_conditions)
print "Amount conditions is %d" % amount_conditions

case = 1
fails = 0
estimated = 0
results = []
for input_index in xrange(amount_conditions):
    for output_index in xrange(amount_conditions):

        in_cond = input_conditions.get_condition(input_index)
        out_cond = output_conditions.get_condition(output_index)

        print "=" * 50 + "start" + "=" * 50
        case_results = []
        print "case is %d" % (case + 1)
        case += 1
        # if case < 37:
        #     continue
        # if case > 37:
        #     exit(0)
        print "Input condition ", str(in_cond)
        print "Output condition ", str(out_cond)

        new_system = system.copy()
        # print "got next system: \n", new_system
        new_system.apply_common_condition(in_cond)
        new_system.apply_common_condition(out_cond)
        print "after apply conditions: \n", new_system
        custom_cond = CustomConditions()
        while new_system.has_condition():
            # print "-"*20 + "iteration start" + "-"*20
            new_system.analyse_and_set_custom_conditions(custom_cond)
            # print "after system analyse: \n", new_system
            # print "all custom conditions: ",  custom_cond
            new_system.apply_custom_conditions(custom_cond)
            # print "after apply custom conditions: \n", new_system
            # print "-"*20 + "iteration end" + "-"*20

        print "after system analyse: \n", new_system
        print "all custom conditions: ",  custom_cond
        if custom_cond.exist_contradiction(in_cond, out_cond):
            print "New system has contradiction conditions."
            print "FAIL SYSTEM!!!!"
            fails += 1
            case_results.append("Fail")
        elif new_system.do_fast_estimation(custom_cond, in_cond, out_cond):
            print "CAN BE ESTIMATED  p^%d!!! All primitive transitions" % len(new_system)
            estimated += 1
            case_results.append("p^%d" % len(new_system))
        else:
            print "all custom conditions: ",  custom_cond
            print "after applying conditions: \n", new_system
            print "=" * 50 + "end" + "=" * 50
            SystemTransition.estimate(
                new_system, custom_cond, in_cond, out_cond, case_results, False)

        print "case res = " + str(case_results)
        results.append(case_results)
        print "=" * 150

print "Total fails is %d" % fails
print "Total estimated is %d" % estimated


def remove_empty(lst):
    while '' in lst:
        lst.remove('')

    for x in xrange(len(lst)):
        if isinstance(lst[x], list):
            remove_empty(lst[x])


def handle_list(lst):
    for x in xrange(len(lst)):
        if isinstance(lst[x], list):
            if len(lst[x]) > 1:
                handle_list(lst[x])
            if len(lst[x]) == 1:
                if lst[x][0] == 'fork':
                    lst[x] = ''
                else:
                    res = lst[x][0]
                    lst[x] = res
                    if isinstance(lst[x], list):
                        handle_list(lst[x])
        if isinstance(lst[x], list):
            # print "again list" + str(lst[x])
            handle_list(lst[x])


def replace_forks(lst):
    for x in xrange(len(lst)):
        if isinstance(lst[x], list):
            # assert lst[x][0] == 'fork'
            if not all(isinstance(elem, str) for elem in lst[x]):
                replace_forks(lst[x])

            if all(isinstance(elem, str) for elem in lst[x]) and(
                    len(lst[x]) > 0 and lst[x][0] == 'fork'):

                fork = " + ".join(lst[x])
                lst[x] = fork[7:]   # cut word 'fork'


def collect_estimates(lst):
    for x in xrange(len(lst)):
        estimate = lst[x]
        # print str(estimate)
        res = estimate.split(' + ')
        if len(res) > 1:
            print "[collect_estimates] res = " + str(res)
            new_res = sorted(res, key=lambda est: int(est[2]), reverse=True)
            # print "sorted " + str(new_res)
            final_str = ''
            value = 0
            while len(new_res) > 0:
                elem = new_res.pop(0)
                count = new_res.count(elem) + 1
                final_str += " + %d*%s" % (count, elem)
                value += count * pow(0.5, int(elem[2]))
                while len(new_res) > 0 and new_res[0] == elem:
                    new_res.pop(0)
            lst[x] = (final_str[3:], value)
        elif res[0] != "Fail":
            lst[x] = (res[0], pow(0.5, int(res[0][2])))
        else:
            lst[x] = (res[0], -1)


print "Total results is "
# pos, estimate, value
max_est = (0, 0, -1)
for x in xrange(len(results)):

    print "%d) before %s" % (x + 1, str(results[x]))
    handle_list(results[x])
    print "%d) before2 %s" % (x + 1, str(results[x]))
    remove_empty(results[x])
    print "%d) before3 %s" % (x + 1, str(results[x]))
    replace_forks(results[x])

    if isinstance(results[x][0], list):
        results[x] = results[x][0]
    print "%d) after %s" % (x + 1, str(results[x]))
    collect_estimates(results[x])
    print "%d) %s" % (x + 1, str(results[x]))
    for value in results[x]:
        if value[1] > max_est[2]:
            max_est = (x + 1, value[0], value[1])

print "\nMax estimation is " + str(max_est)
