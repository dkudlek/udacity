#! /usr/bin/env python3
#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(probability_vect, movement):
    if movement == 0:
        return probability_vect
    length = len(probability_vect)
    i = (len(probability_vect) - movement) % length
    result_vect=[]
    for j in range(len(probability_vect)):
      result_vect.append(probability_vect[(i + j) % length])
    return result_vect

myRoundedOldList = [ round(elem, 2) for elem in p ]
print("old:         ", myRoundedOldList)
#print "world:       ", world
p = move(p, 1)
myRoundedNewList = [ round(elem, 2) for elem in p ]
print("new:         ", myRoundedNewList)
print("")
