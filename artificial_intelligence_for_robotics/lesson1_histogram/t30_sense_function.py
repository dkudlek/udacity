#! /usr/bin/env python3
#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    success = []
    for i in range(0, len(p)):
        if(world[i] == Z):
            p[i] = p[i] * pHit
            success.append("hit")
        else:
            p[i] = p[i] * pMiss
            success.append("miss")
    q = p
    return q, success

print("old:         ",p)
print("world:       ",world)
print("observation: ", Z)
p, succ = sense(p,Z)
myRoundedList = [ round(elem, 2) for elem in p ]
print("hit/miss:    ",succ)
print("new:         ",myRoundedList)
