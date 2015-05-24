from variable import TypeVariable
from variable import Variable
from side import Side
from transition import Transition
from transition import SystemTransition
#from conditions import Condition
from conditions import CommonConditions


a1 = Variable(TypeVariable.INPUT)
a2 = Variable(TypeVariable.INPUT)
a3 = Variable(TypeVariable.INPUT)

g1 = Variable(TypeVariable.OUTPUT)
g2 = Variable(TypeVariable.OUTPUT)
g3 = Variable(TypeVariable.OUTPUT)

b1 = Variable(TypeVariable.UNKNOWN)
b2 = Variable(TypeVariable.UNKNOWN)
b3 = Variable(TypeVariable.UNKNOWN)


t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, g1))
t5 = Transition(Side(b2), Side(b3, g1, g2))
t6 = Transition(Side(b3), Side(g1, g2, g3))

system = SystemTransition(t1, t2, t3, t4, t5, t6)
print "Basic system is: \n" + str(system) + "\n\n"

com_cond = CommonConditions(a1, a2, a3)
print "generating ..."
print com_cond.generate_conditions()

for index in xrange(com_cond.get_amount_conditions()):
    cond = com_cond.get_common_cond(index)
    print "Condition: %s" % "; ".join(map(str, cond))
    print "complem cond => %s" % "; ".join(
        map(str, com_cond.get_complem_com_cond(index))
    )
    new_system = system.copy_with_cond(cond)
    print "got next system: "
    print str(new_system) + "\n\n"
