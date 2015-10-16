#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from polygon_color import plot_boundary
import readfile

points = [(3, 9),(3, 18),(6, 30),(12, 42),(15, 9),(15, 42),(21, 21),(32, 33),(35, 24),(35, 51),(47, 30)]

def convex_hull_plot(file):
    
    result = readfile.readfile(file)
    points = result['points']
    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    hull = convex_hull(points)
    plt.scatter(*zip(*points))
    plot_boundary(hull)
    plt.show(block=False)

def convex_hull(points):
    if (len(points) <= 3):
        hull = brute_force(points)
    else:
        midpoint = len(points)/2
        lA = [points[i] for i in range(midpoint)]
        lB = [points[i+midpoint] for i in range(len(points)-midpoint)]       
        hA = convex_hull(lA)
        hB = convex_hull(lB)
        hull = merge_hulls(hA,hB)     
    return hull
              
def brute_force(points):
    if len(points)==3:
        dir = check_turn_dir(points[0],points[1],points[2])
        if dir<0:
            points = [points[0], points[2], points[1]]
        return points
    else:
        return points
        
def merge_hulls(lA,lB):
# Find the upper tangent
    rightA_top = lA.index(max(lA, key=lambda x:x[0]))
    leftB_top = lB.index(min(lB, key=lambda x:x[0]))
    upperright = check_turn_dir(lA[rightA_top],lB[leftB_top],lB[(leftB_top-1)%len(lB)])
    upperleft = check_turn_dir(lB[leftB_top],lA[rightA_top],lA[(rightA_top+1)%len(lA)])
    while (upperright > 0) or (upperleft < 0):
        if (upperright > 0):
            leftB_top = (leftB_top - 1)%len(lB)
        elif (upperleft < 0):
            rightA_top = (rightA_top + 1)%len(lA)
        upperright = check_turn_dir(lA[rightA_top],lB[leftB_top],lB[(leftB_top-1)%len(lB)])
        upperleft = check_turn_dir(lB[leftB_top],lA[rightA_top],lA[(rightA_top+1)%len(lA)])

# Find the lower tangent
    rightA_bot = lA.index(max(lA, key=lambda x:x[0]))
    leftB_bot = lB.index(min(lB, key=lambda x:x[0]))
    lowerright = check_turn_dir(lA[rightA_bot],lB[leftB_bot],lB[(leftB_bot+1)%len(lB)])
    lowerleft = check_turn_dir(lB[leftB_bot],lA[rightA_bot],lA[(rightA_bot-1)%len(lA)])
    while (lowerright < 0) or (lowerleft > 0):
        if (lowerright < 0):
            leftB_bot = (leftB_bot + 1)%len(lB)
        elif (lowerleft > 0):
            rightA_bot = (rightA_bot - 1)%len(lA)
        lowerright = check_turn_dir(lA[rightA_bot],lB[leftB_bot],lB[(leftB_bot+1)%len(lB)])
        lowerleft = check_turn_dir(lB[leftB_bot],lA[rightA_bot],lA[(rightA_bot-1)%len(lA)])
#Step clockwise around hull using tangents
    P3 = []
    nodeA = rightA_top
    P3.append(lA[nodeA])
    nodeA = (nodeA + 1)%len(lA)
    while (nodeA != rightA_bot):
        P3.append(lA[nodeA])
        nodeA = (nodeA + 1)%len(lA)
    P3.append(lA[nodeA])
    nodeB = leftB_bot
    P3.append(lB[nodeB])
    nodeB = (nodeB + 1)%len(lB)
    while (nodeB != leftB_top):
        P3.append(lB[nodeB])
        nodeB = (nodeB + 1)%len(lB)
    P3.append(lB[nodeB])
    return P3
         
def check_turn_dir(p1,p2,p3):
    seg1 = [a - b for a,b in zip(p2,p1)]
    seg2 = [a - b for a,b in zip(p3,p2)]
    dir = np.cross(seg1,seg2)
    return dir

if __name__ == '__main__':
    convex_hull_plot(points)
