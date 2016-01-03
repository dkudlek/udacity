#! /usr/bin/env python3
#Modify your code so that it normalizes the output for
#the function sense. This means that the entries in q
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    hits=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        hits.append(hit)
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    q_sum = sum(q)
    for i in range(len(q)):
        q[i] = q[i]/q_sum
    assert abs(sum(q)-1) <= 0.00001
    return q, hits


print("old:         ",p)
print("world:       ",world)
print("observation: ", Z)
p, succ = sense(p,Z)
myRoundedList = [ round(elem, 2) for elem in p ]
print("hit/miss:    ",succ)
print("new:         ",myRoundedList)
