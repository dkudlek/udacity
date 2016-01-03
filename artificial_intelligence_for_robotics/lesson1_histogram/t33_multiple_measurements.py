#! /usr/bin/env python3
#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both
#measurements are incorporated. Make sure that your code
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
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
#
#ADD YOUR CODE HERE
#
for i in range(len(measurements)):
    myRoundedOldList = [ round(elem, 2) for elem in p ]
    print("old:         ", myRoundedOldList)
    print("world:       ", world)
    print("observation: ", measurements[i])
    p, succ = sense(p,measurements[i])
    myRoundedNewList = [ round(elem, 2) for elem in p ]
    print("hit/miss:    ", succ)
    print("new:         ", myRoundedNewList)
    print("")
