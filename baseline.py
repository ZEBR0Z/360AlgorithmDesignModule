import sys

# Input:
# O -> array of orange trees
# C -> array of Cactus trees
# S / S_i -> array of sprinklers
# R / R_i -> Radius of sprinklers
O = []
C = []
S = []
R = []

# Problem:
#  Select an arrangement of sprinklers such that
#  Restriction 1: All orange trees are watered
#  Restriction 2: Minimize number of cacti watered

# My intial thoughts reading throughout the problem, the initial restriction is a subset optimization/combinatrics search
# and the second restriction is a optimization problem. 

orange_inp = input().split()
for i in orange_inp:
    O.append(int(i))

cactus_inp = input().split()
for i in cactus_inp:
    C.append(int(i))

sprinkler_inp = input().split()
for i in sprinkler_inp:
    S.append(int(i))

radius_inp = input().split()
for i in radius_inp:
    R.append(int(i))


