#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

points = [(3, 9),(3, 18),(6, 30),(12, 33),(12, 42),(15, 9),(15, 24),(15, 42),(15, 51),(21, 21),(27, 30)]

def convex_hull(points):
    plt.plot(*zip(*points), marker='.', markersize = 25)
    plt.show()
    if (len(points) <= 3):
        hull = brute_force(points)
    else:
        midpoint = len(points)/2
        lA = [points[i] for i in range(midpoint)]
        lB = [points[i+midpoint] for i in range(len(points)-midpoint)]
        hA = convex_hull(A)
        hB = convex_hull(B)
        seg = 
        
        
    
    
    
    
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
