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


# t1 = Transition(Side(a1), Side(a2, a3, b1))
# t2 = Transition(Side(a2), Side(a3, b1, b2))
# t3 = Transition(Side(a3), Side(b1, b2, b3))
# t4 = Transition(Side(b1), Side(b2, b3, g1))
# t5 = Transition(Side(b2), Side(b3, g1, g2))
# t6 = Transition(Side(b3), Side(g1, g2, g3))


t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, g1))
t4 = Transition(Side(b1), Side(b2, g1, g2))
t5 = Transition(Side(b2), Side(g1, g2, g3))

system = SystemTransition(t1, t2, t3, t4, t5)
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

print "Total results is "
for x in xrange(len(results)):
    print "%d) %s" % (x + 1, str(results[x]))
