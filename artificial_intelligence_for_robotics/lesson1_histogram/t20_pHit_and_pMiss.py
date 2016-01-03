#! /usr/bin/env python3
#Write code that outputs p after multiplying each entry
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.

world = ["miss", "hit", "hit", "miss", "miss"]
p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
p_old = p

for i in range(0, len(p)):
    if (i == 1 or i == 2):
        p[i] = p[i] * pHit
    else:
        p[i] = p[i] * pMiss

print(p_old)
print(world)
print(p)
