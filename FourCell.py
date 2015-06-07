from variable import Variable
from variable import TypeVariable
from side import Side
from transition import Transition
from transition import SystemTransition

a1 = Variable(TypeVariable.INPUT)
a2 = Variable(TypeVariable.INPUT)
a3 = Variable(TypeVariable.INPUT)
a4 = Variable(TypeVariable.INPUT)
a5 = Variable(TypeVariable.INPUT)

g1 = Variable(TypeVariable.OUTPUT)
g2 = Variable(TypeVariable.OUTPUT)
g3 = Variable(TypeVariable.OUTPUT)
g4 = Variable(TypeVariable.OUTPUT)
g5 = Variable(TypeVariable.OUTPUT)

b1 = Variable(TypeVariable.UNKNOWN)
b2 = Variable(TypeVariable.UNKNOWN)
b3 = Variable(TypeVariable.UNKNOWN)
b4 = Variable(TypeVariable.UNKNOWN)
b5 = Variable(TypeVariable.UNKNOWN)
b6 = Variable(TypeVariable.UNKNOWN)
b7 = Variable(TypeVariable.UNKNOWN)
b8 = Variable(TypeVariable.UNKNOWN)
b9 = Variable(TypeVariable.UNKNOWN)
b10 = Variable(TypeVariable.UNKNOWN)
b11 = Variable(TypeVariable.UNKNOWN)

# 3 blocks
three_blocks_systems = {}

# 4 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, g1))
t3 = Transition(Side(a3), Side(b1, g1, g2))
t4 = Transition(Side(b1), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4)
three_blocks_systems["4"] = system

# 5 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, g1))
t4 = Transition(Side(b1), Side(b2, g1, g2))
t5 = Transition(Side(b2), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5)
three_blocks_systems["5"] = system

# 6 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, g1))
t5 = Transition(Side(b2), Side(b3, g1, g2))
t6 = Transition(Side(b3), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6)
three_blocks_systems["6"] = system

# 7 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, g1))
t6 = Transition(Side(b3), Side(b4, g1, g2))
t7 = Transition(Side(b4), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7)
three_blocks_systems["7"] = system

# 8 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, g1))
t7 = Transition(Side(b4), Side(b5, g1, g2))
t8 = Transition(Side(b5), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8)
three_blocks_systems["8"] = system

# 9 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, g1))
t8 = Transition(Side(b5), Side(b6, g1, g2))
t9 = Transition(Side(b6), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9)
three_blocks_systems["9"] = system

# 10 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, b7))
t8 = Transition(Side(b5), Side(b6, b7, g1))
t9 = Transition(Side(b6), Side(b7, g1, g2))
t10 = Transition(Side(b7), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
three_blocks_systems["10"] = system

# 11 rounds
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
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)
three_blocks_systems["11"] = system

# 12 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, b7))
t8 = Transition(Side(b5), Side(b6, b7, b8))
t9 = Transition(Side(b6), Side(b7, b8, b9))
t10 = Transition(Side(b7), Side(b8, b9, g1))
t11 = Transition(Side(b8), Side(b9, g1, g2))
t12 = Transition(Side(b9), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
three_blocks_systems["12"] = system

# 13 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, b7))
t8 = Transition(Side(b5), Side(b6, b7, b8))
t9 = Transition(Side(b6), Side(b7, b8, b9))
t10 = Transition(Side(b7), Side(b8, b9, b10))
t11 = Transition(Side(b8), Side(b9, b10, g1))
t12 = Transition(Side(b9), Side(b10, g1, g2))
t13 = Transition(Side(b10), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13)
three_blocks_systems["13"] = system

# 14 rounds
t1 = Transition(Side(a1), Side(a2, a3, b1))
t2 = Transition(Side(a2), Side(a3, b1, b2))
t3 = Transition(Side(a3), Side(b1, b2, b3))
t4 = Transition(Side(b1), Side(b2, b3, b4))
t5 = Transition(Side(b2), Side(b3, b4, b5))
t6 = Transition(Side(b3), Side(b4, b5, b6))
t7 = Transition(Side(b4), Side(b5, b6, b7))
t8 = Transition(Side(b5), Side(b6, b7, b8))
t9 = Transition(Side(b6), Side(b7, b8, b9))
t10 = Transition(Side(b7), Side(b8, b9, b10))
t11 = Transition(Side(b8), Side(b9, b10, b11))
t12 = Transition(Side(b9), Side(b10, b11, g1))
t13 = Transition(Side(b10), Side(b11, g1, g2))
t14 = Transition(Side(b11), Side(g1, g2, g3))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14)
three_blocks_systems["14"] = system


# 4 blocks
four_blocks_systems = {}

# 4 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, g1))
t2 = Transition(Side(a2), Side(a3, a4, g1, g2))
t3 = Transition(Side(a3), Side(a4, g1, g2, g3))
t4 = Transition(Side(a4), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4)
four_blocks_systems["4"] = system

# 5 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, g1))
t3 = Transition(Side(a3), Side(a4, b1, g1, g2))
t4 = Transition(Side(a4), Side(b1, g1, g2, g3))
t5 = Transition(Side(b1), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5)
four_blocks_systems["5"] = system

# 6 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, g1))
t4 = Transition(Side(a4), Side(b1, b2, g1, g2))
t5 = Transition(Side(b1), Side(b2, g1, g2, g3))
t6 = Transition(Side(b2), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6)
four_blocks_systems["6"] = system

# 7 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, g1))
t5 = Transition(Side(b1), Side(b2, b3, g1, g2))
t6 = Transition(Side(b2), Side(b3, g1, g2, g3))
t7 = Transition(Side(b3), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7)
four_blocks_systems["7"] = system

# 8 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, g1))
t6 = Transition(Side(b2), Side(b3, b4, g1, g2))
t7 = Transition(Side(b3), Side(b4, g1, g2, g3))
t8 = Transition(Side(b4), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8)
four_blocks_systems["8"] = system

# 9 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, g1))
t7 = Transition(Side(b3), Side(b4, b5, g1, g2))
t8 = Transition(Side(b4), Side(b5, g1, g2, g3))
t9 = Transition(Side(b5), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9)
four_blocks_systems["9"] = system

# 10 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, b6))
t7 = Transition(Side(b3), Side(b4, b5, b6, g1))
t8 = Transition(Side(b4), Side(b5, b6, g1, g2))
t9 = Transition(Side(b5), Side(b6, g1, g2, g3))
t10 = Transition(Side(b6), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
four_blocks_systems["10"] = system

# 11 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, b6))
t7 = Transition(Side(b3), Side(b4, b5, b6, b7))
t8 = Transition(Side(b4), Side(b5, b6, b7, g1))
t9 = Transition(Side(b5), Side(b6, b7, g1, g2))
t10 = Transition(Side(b6), Side(b7, g1, g2, g3))
t11 = Transition(Side(b7), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)
four_blocks_systems["11"] = system

# 12 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, b6))
t7 = Transition(Side(b3), Side(b4, b5, b6, b7))
t8 = Transition(Side(b4), Side(b5, b6, b7, b8))
t9 = Transition(Side(b5), Side(b6, b7, b8, g1))
t10 = Transition(Side(b6), Side(b7, b8, g1, g2))
t11 = Transition(Side(b7), Side(b8, g1, g2, g3))
t12 = Transition(Side(b8), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
four_blocks_systems["12"] = system

# 13 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, b6))
t7 = Transition(Side(b3), Side(b4, b5, b6, b7))
t8 = Transition(Side(b4), Side(b5, b6, b7, b8))
t9 = Transition(Side(b5), Side(b6, b7, b8, b9))
t10 = Transition(Side(b6), Side(b7, b8, b9, g1))
t11 = Transition(Side(b7), Side(b8, b9, g1, g2))
t12 = Transition(Side(b8), Side(b9, g1, g2, g3))
t13 = Transition(Side(b9), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13)
four_blocks_systems["13"] = system

# 14 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, b1))
t2 = Transition(Side(a2), Side(a3, a4, b1, b2))
t3 = Transition(Side(a3), Side(a4, b1, b2, b3))
t4 = Transition(Side(a4), Side(b1, b2, b3, b4))
t5 = Transition(Side(b1), Side(b2, b3, b4, b5))
t6 = Transition(Side(b2), Side(b3, b4, b5, b6))
t7 = Transition(Side(b3), Side(b4, b5, b6, b7))
t8 = Transition(Side(b4), Side(b5, b6, b7, b8))
t9 = Transition(Side(b5), Side(b6, b7, b8, b9))
t10 = Transition(Side(b6), Side(b7, b8, b9, b10))
t11 = Transition(Side(b7), Side(b8, b9, b10, g1))
t12 = Transition(Side(b8), Side(b9, b10, g1, g2))
t13 = Transition(Side(b9), Side(b10, g1, g2, g3))
t14 = Transition(Side(b10), Side(g1, g2, g3, g4))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14)
four_blocks_systems["14"] = system


# 5 blocks
five_blocks_systems = {}

# 5 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, g1))
t2 = Transition(Side(a2), Side(a3, a4, a5, g1, g2))
t3 = Transition(Side(a3), Side(a4, a5, g1, g2, g3))
t4 = Transition(Side(a4), Side(a5, g1, g2, g3, g4))
t5 = Transition(Side(a5), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5)
five_blocks_systems["5"] = system

# 6 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, g1))
t3 = Transition(Side(a3), Side(a4, a5, b1, g1, g2))
t4 = Transition(Side(a4), Side(a5, b1, g1, g2, g3))
t5 = Transition(Side(a5), Side(b1, g1, g2, g3, g4))
t6 = Transition(Side(b1), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6)
five_blocks_systems["6"] = system

# 7 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, g1))
t4 = Transition(Side(a4), Side(a5, b1, b2, g1, g2))
t5 = Transition(Side(a5), Side(b1, b2, g1, g2, g3))
t6 = Transition(Side(b1), Side(b2, g1, g2, g3, g4))
t7 = Transition(Side(b2), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7)
five_blocks_systems["7"] = system

# 8 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, g1))
t5 = Transition(Side(a5), Side(b1, b2, b3, g1, g2))
t6 = Transition(Side(b1), Side(b2, b3, g1, g2, g3))
t7 = Transition(Side(b2), Side(b3, g1, g2, g3, g4))
t8 = Transition(Side(b3), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8)
five_blocks_systems["8"] = system

# 9 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, g1))
t6 = Transition(Side(b1), Side(b2, b3, b4, g1, g2))
t7 = Transition(Side(b2), Side(b3, b4, g1, g2, g3))
t8 = Transition(Side(b3), Side(b4, g1, g2, g3, g4))
t9 = Transition(Side(b4), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9)
five_blocks_systems["9"] = system

# 10 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, b5))
t6 = Transition(Side(b1), Side(b2, b3, b4, b5, g1))
t7 = Transition(Side(b2), Side(b3, b4, b5, g1, g2))
t8 = Transition(Side(b3), Side(b4, b5, g1, g2, g3))
t9 = Transition(Side(b4), Side(b5, g1, g2, g3, g4))
t10 = Transition(Side(b5), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10)
five_blocks_systems["10"] = system

# 11 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, b5))
t6 = Transition(Side(b1), Side(b2, b3, b4, b5, b6))
t7 = Transition(Side(b2), Side(b3, b4, b5, b6, g1))
t8 = Transition(Side(b3), Side(b4, b5, b6, g1, g2))
t9 = Transition(Side(b4), Side(b5, b6, g1, g2, g3))
t10 = Transition(Side(b5), Side(b6, g1, g2, g3, g4))
t11 = Transition(Side(b6), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11)
five_blocks_systems["11"] = system

# 12 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, b5))
t6 = Transition(Side(b1), Side(b2, b3, b4, b5, b6))
t7 = Transition(Side(b2), Side(b3, b4, b5, b6, b7))
t8 = Transition(Side(b3), Side(b4, b5, b6, b7, g1))
t9 = Transition(Side(b4), Side(b5, b6, b7, g1, g2))
t10 = Transition(Side(b5), Side(b6, b7, g1, g2, g3))
t11 = Transition(Side(b6), Side(b7, g1, g2, g3, g4))
t12 = Transition(Side(b7), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12)
five_blocks_systems["12"] = system

# 13 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, b5))
t6 = Transition(Side(b1), Side(b2, b3, b4, b5, b6))
t7 = Transition(Side(b2), Side(b3, b4, b5, b6, b7))
t8 = Transition(Side(b3), Side(b4, b5, b6, b7, b8))
t9 = Transition(Side(b4), Side(b5, b6, b7, b8, g1))
t10 = Transition(Side(b5), Side(b6, b7, b8, g1, g2))
t11 = Transition(Side(b6), Side(b7, b8, g1, g2, g3))
t12 = Transition(Side(b7), Side(b8, g1, g2, g3, g4))
t13 = Transition(Side(b8), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13)
five_blocks_systems["13"] = system


# 14 rounds
t1 = Transition(Side(a1), Side(a2, a3, a4, a5, b1))
t2 = Transition(Side(a2), Side(a3, a4, a5, b1, b2))
t3 = Transition(Side(a3), Side(a4, a5, b1, b2, b3))
t4 = Transition(Side(a4), Side(a5, b1, b2, b3, b4))
t5 = Transition(Side(a5), Side(b1, b2, b3, b4, b5))
t6 = Transition(Side(b1), Side(b2, b3, b4, b5, b6))
t7 = Transition(Side(b2), Side(b3, b4, b5, b6, b7))
t8 = Transition(Side(b3), Side(b4, b5, b6, b7, b8))
t9 = Transition(Side(b4), Side(b5, b6, b7, b8, b9))
t10 = Transition(Side(b5), Side(b6, b7, b8, b9, g1))
t11 = Transition(Side(b6), Side(b7, b8, b9, g1, g2))
t12 = Transition(Side(b7), Side(b8, b9, g1, g2, g3))
t13 = Transition(Side(b8), Side(b9, g1, g2, g3, g4))
t14 = Transition(Side(b9), Side(g1, g2, g3, g4, g5))
system = SystemTransition(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14)
five_blocks_systems["14"] = system
