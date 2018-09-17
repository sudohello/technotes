---
title: Algo & Math
---

**Table of Contents**
* TOC
{:toc}


## Alogrithms
* k-means clustering
* ICP - Iterative Closest Point [automatic 3D data registration]
* Greedy
* SFM-DMVR algorithms
* bundle adjustment
* iso-surface extraction
  * marching cubes
* SAD - Sum of Absolute Difference [Disparity generation]
* RANSAC - Random Sample Consensus
* SSD - Sum of Square Differences

# Mathematics

## Math Concepts

### Propability Distribution
**keywords**: posterior distribution, localization, measurement update, probability distribution, Theorem of Probability, Convolution

$P(Xi|Z)$

**From Udacity course quiz**
```
p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    s=0.0
    for i in range(len(p)):
        hit = (Z == world[i])
        j=p[i] * (hit * pHit + (1-hit) * pMiss)
        s=s+j
        q.append(j)
    for i in range(len(p)):
        q[i]=q[i]/s
    return q
print sense(p,Z)
```

```
#Given the list motions=[1,1] which means the robot
#moves right and then right again, compute the posterior
#distribution if the robot first senses red, then moves
#right one, then senses green, then moves right again,
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
#
# ADD CODE HERE
#
print p
```
