#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

points = [(3, 9),(3, 18),(6, 30),(12, 33),(12, 42),(15, 9),(15, 24),(15, 42),(15, 51),(21, 21),(27, 30)]
#        P1 = [(21,21),(15,42),(12,42),(6,30),(3,18),(3,9),(15,9)]
#        P2 = [(35,24),(47,30),(35,51),(32,33)]

def convex_hull_plot(points):
    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    hull = convex_hull(points)
    plt.plot(*zip(*points), marker='.', markersize = 25)
    plt.plot(*zip(*hull), marker='.', markersize = 25)
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
        hull = merge_hulls(lA,lB)     
        raw_input('Next')
        print(hull)
        return hull
              
def merge_hulls(P1,P2):
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
        
def brute_force(points):
    dir = check_turn_dir(points[0],points[1],points[2])
    if dir<0:
        points = [points[0], points[2], points[1]]
    return points

        
        
    
    
    
    
#    def flood_fill(x, y, OldColor, NewColor, xmin, ymin, colors):
#    if (colors[x - xmin][y - ymin] == OldColor):      
#        plt.plot(x, y, marker='.', markersize = 15, markerfacecolor = 'g')
#        colors[x-xmin][y-ymin] = NewColor
#        flood_fill(x,y-1,OldColor, NewColor, xmin, ymin, colors)
#        flood_fill(x,y+1,OldColor, NewColor, xmin, ymin, colors)
#        flood_fill(x-1,y,OldColor, NewColor, xmin, ymin, colors)
#        flood_fill(x+1,y,OldColor, NewColor, xmin, ymin, colors)



if __name__ == '__main__':
    convex_hull(points)
