from variable import TypeVariable
from variable import Variable
from side import Side
from transition import Transition
from transition import SystemTransition
# from conditions import Condition
from conditions import CommonConditions
from conditions import CustomConditions
from test_for_res import get_normalise_result

from SMS4 import three_blocks_systems
from SMS4 import a1
from SMS4 import a2
from SMS4 import a3
from SMS4 import g1
from SMS4 import g2
from SMS4 import g3


def main(system, inputs, outputs):

    print "Basic system is: \n" + str(system) + "\n\n"

    print "Creating common conditions..."
    input_conditions = CommonConditions(*inputs)
    output_conditions = CommonConditions(*outputs)

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
            comcon_nz = list(in_cond.get_non_zero_condition())
            comcon_nz.extend(out_cond.get_non_zero_condition())

            print "=" * 50 + "start" + "=" * 50
            case_results = []
            print "case is %d" % (case + 1)
            case += 1
            if case < 50:
                continue
            if case > 50:
                exit(0)
            print "Input condition ", str(in_cond)
            print "Output condition ", str(out_cond)

            new_system = system.copy()
            # print "got next system: \n", new_system
            new_system.apply_common_condition(in_cond)
            new_system.apply_common_condition(out_cond)
            print "after apply conditions: \n", new_system
            custom_cond = CustomConditions()
            new_system.simplify_with_custom_conditions(custom_cond)
            print "after system analyse: \n", new_system
            print "all custom conditions: ",  custom_cond
            if custom_cond.exist_contradiction(comcon_nz):
                print "New system has contradiction conditions."
                print "FAIL SYSTEM!!!!"
                fails += 1
                case_results.append(("Fail", -1))
            elif new_system.do_fast_estimation(custom_cond, comcon_nz):
                print "CAN BE ESTIMATED  p^%d!!! All primitive transitions" % len(new_system)
                estimated += 1
                case_results.append(("p^%d" % len(new_system), pow(0.5, len(new_system))))
            else:
                print "all custom conditions: ",  custom_cond
                print "after applying conditions: \n", new_system
                print "=" * 50 + "end" + "=" * 50
                SystemTransition.estimate(
                    new_system, custom_cond, in_cond, out_cond,
                    comcon_nz, case_results, False)

            print "case res = " + str(case_results)
            results.append(case_results)
            print "=" * 150

    print "Total fails is %d" % fails
    print "Total estimated is %d" % estimated

    print "+" * 120
    for x in xrange(len(results)):
        print "%d) %s" % (x + 1, str(results[x]))
    print "+" * 120

    max_est = (0, 0, -1)
    for x in xrange(len(results)):

        print "%d) before %s" % (x + 1, str(results[x]))
        get_normalise_result(results[x])
        print "%d) after %s" % (x + 1, str(results[x]))

        while '' in results[x]:
            results[x].remove('')

        for value in results[x]:
            if value[1] > max_est[2]:
                max_est = (x + 1, value[0], value[1])
                print "NEW MAX " + str(max_est)

    print "\nMax estimation is " + str(max_est)

    final_str = ''
    res = max_est[1].split(' + ')
    while '' in res:
        res.remove('')

    length = len(res)
    if length > 1:
        # print "[collect_estimates] res = " + str(res)
        new_res = sorted(res, key=lambda est: int(est[2]), reverse=True)
        # print "sorted " + str(new_res)
        while len(new_res) > 0:
            elem = new_res.pop(0)
            count = new_res.count(elem) + 1
            final_str += " + %d*%s" % (count, elem)
            while len(new_res) > 0 and new_res[0] == elem:
                new_res.pop(0)
        final_str = final_str[3:]
        print "in siplify form = " + final_str
    elif length == 1:
        final_str = res[0] if len(res) == 1 else 'MORE THAN ONE'
        print ":("
    else:
        final_str = "emply list"

    print final_str

    return (str(max_est), final_str)


f = open('3_block_sms4_res', 'w+', 0)

for key, value in three_blocks_systems.items():
    res = main(value, [a1, a2, a3], [g1, g2, g3])
    f.write("%s blocks: %s\n" % (str(key), str(res)))
    f.flush()

f.close()
