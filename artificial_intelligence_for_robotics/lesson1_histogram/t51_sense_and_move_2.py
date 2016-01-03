#! /usr/bin/env python3
#Modify the previous code so that the robot senses red twice.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

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

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for i in range(len(motions)):
    myRoundedOldList = [ round(elem, 2) for elem in p ]
    print("old:         ", myRoundedOldList)
    print("world:       ", world)
    print("observation: ", measurements[i])
    p, succ = sense(p,measurements[i])
    myRoundedNewList = [ round(elem, 2) for elem in p ]
    print("hit/miss:    ", succ)
    print("sense:       ", myRoundedNewList)
    print("motion:      ", motions[i])
    p = move(p,motions[i])
    myRoundedNewList = [ round(elem, 2) for elem in p ]
    print("move:        ", myRoundedNewList)
    print("")
