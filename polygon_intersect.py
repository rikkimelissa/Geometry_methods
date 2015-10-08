#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def polygon_intersect():
# find_intersections():
# find_polygons():
    P1 = [(7,7),(5,14),(4,14),(2,10),(1,6),(1,3),(5,3)]
    P2 = [(5,8),(9,10),(5,17),(4,11)]
    
def find_intersections(P1,P2):
    #line sweep
    x1 = [P1[i][0] for i in range(len(P1))]
    y1 = [P1[i][1] for i in range(len(P1))]
    x2 = [P2[i][0] for i in range(len(P2))]
    y2 = [P2[i][1] for i in range(len(P2))]
    ylist = np.sort(y1 + y2)
    ylabels = [1]*len(y1) + [2]*len(y2)
    eventlist = ylist[::-1]
    ylist_ind = np.argsort(y1 + y2)
    order = ylist_ind[::-1]
    segmentlist = []
    for y, ind in zip(eventlist,order):
        if (ylabels[ind] == 1):
            segment1 = [((x1)[ind-1],(y1)[ind-1]),((x1)[ind],(y1)[ind])]
            segment2 = [((x1)[ind],(y1)[ind]),((x1)[(ind+1)%len(x1)],(y1)[(ind+1)%len(x1)])]
        else:
            ind -= len(x1)
            segment1 = [((x2)[ind-1],(y2)[ind-1]),((x2)[ind],(y2)[ind])]
            segment2 = [((x2)[ind],(y2)[ind]),((x2)[(ind+1)%len(y2)],(y2)[(ind+1)%len(y2)])]
        if not segment1 in segmentlist
            segmentlist.append(segment1)
        if not segment2 in segmentlist
            segmentlist.append(segment2)
        for i,segments_y in enumerate(segmentlist):
            if segments_y[0][1] > y and segments_y[1][1] > y:
                 del segmentlist[i]
        
        
        
        
        
        
def line_intersect(l1,l2):
# http://www.ahinson.com/algorithms_general/Sections/Geometry/ParametricLineIntersection.pdf
    x1 = l1[0][0]
    y1 = l1[0][1]
    x2 = l1[1][0]
    y2 = l1[1][1]
    x3 = l2[0][0]
    y3 = l2[0][1]
    x4 = l2[1][0]
    y4 = l2[1][1]
    s = float((x4-x3)*(y3-y1) - (x3-x1)*(y4-y3))/((x4-x3)*(y2-y1) - (x2-x1)*(y4-y3))
    t = float((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))/((x4-x3)*(y2-y1) - (x2-x1)*(y4-y3))
    if (s>=0 and s<=1 and t>=0 and t<=1):
        x_int = x1 + (x2-x2)*s
        y_int = y1 + (y2-x2)*s
        intersect = True
    else:
        intersect = False
        x_int = False
        y_int = False
    return {'intersect':intersect, 'x_int':x_int, 'y_int':y_int} 
        


if __name__ == '__main__':
    polygon_intersect()
