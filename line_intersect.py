#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from polygon_color import plot_boundary
from polygon_color import plot_line
from polygon_intersect import find_intersections
from convex_hull import check_turn_dir

P = [(21, 21), (15, 42), (12, 42), (6, 30), (3, 18), (3, 9), (15, 9)]
x = [(30,20),(5,40)]

def line_intersect(P,x):
    plt.plot(*zip(*P))
    plt.plot(*zip(*x))
    plt.show(block=False)  
    result = find_intersections(P,x)
    line = [[int(float(j)) for j in i] for i in result['intersectlist']]
    if len(line)==2:
        plot_boundary(line)
    elif len(line)==1:
        P1 = result['P1']
        intercept = result['intersectlist']
        ind = P1.index(intercept[0])
        tri_dir = check_turn_dir(P1[ind],P1[(ind+1)%len(P1)],x[0])
        if (tri_dir>0):
            intercept.append(x[0])
        else:
            intercept.append(x[1])
        print(intercept)
        intercept = [[int(j) for j in i] for i in intercept]
        plot_boundary(intercept)
          
    plt.show(block=False)  

if __name__ == '__main__':
    line_intersect(P,x)
    
