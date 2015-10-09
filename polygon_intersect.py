#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from polygon_color import plot_boundary # how to import?
from polygon_color import flood_fill

P1 = [(21,21),(15,42),(12,42),(6,30),(3,18),(3,9),(15,9)]
P2 = [(15,24),(27,30),(15,51),(12,33)]

def polygon_intersect(P1,P2):

    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    plot_boundary(P2)
    plot_boundary(P1)
    
    result = find_intersections(P1,P2)
    P3 = compose_new_polygon(result)
    P3 = [[int(float(j)) for j in i] for i in P3]
    
    poly = P3
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    x_sorted = np.sort(px) # replace!!!
    y_sorted = np.sort(py) # replace!!!
    colors = plot_boundary(poly)
    flood_fill(int(np.median(px)),int(np.median(py)), 'w', 'g', x_sorted[0], y_sorted[0], colors)
    
    plt.show(block=False)

def compose_new_polygon(result):
    P1 = result['P1']
    P2 = result['P2']
    P3 = []
    intersect_list = result['intersectlist']
    p1_index0 = P1.index(intersect_list[0])
    p2_index0 = P2.index(intersect_list[0])
    p1_index1 = P1.index(intersect_list[1])
    p2_index1 = P2.index(intersect_list[1])
    seg1 = [a - b for a,b in zip(P1[p1_index0 + 1], intersect_list[0])]
    seg2 = [a - b for a,b in zip(intersect_list[0], P2[p2_index0 + 1])]
    tri_dir = np.cross(seg1,seg2)
    if tri_dir > 0:
        P3.append(intersect_list[0])
        node = (p1_index0+1)%len(P2)
        next = P1[node]
        while (next != intersect_list[1]):
            P3.append(next)
            node = (node+1)%len(P1)
            next = P1[node]         
        P3.append(intersect_list[1])
        node = (p2_index1+1)%len(P2)
        next = P2[node]
        while (next != intersect_list[0]):
            P3.append(next)
            node = (node+1)%len(P2)
            next = P2[node]
    else:
        P3.append(intersect_list[0])
        node = (p2_index0+1)%len(P2)
        next = P2[node]
        while (next != intersect_list[1]):
            P3.append(next)
            node = (node+1)%len(P2)
            next = P2[node]
        P3.append(intersect_list[1])
        node = (p1_index1+1)%len(P2)
        next = P1[node]
        while (next != intersect_list[0]):
            P3.append(next)
            node = (node+1)%len(P1)
            next = P1[node] 
    return P3
    
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
    segmentlabels = []
    intersectlist = []
    P1new = P1
    P2new = P2
    for y, ind in zip(eventlist,order):
        if (ylabels[ind] == 1):
            segment1 = [((x1)[ind-1],(y1)[ind-1]),((x1)[ind],(y1)[ind])]
            segment2 = [((x1)[ind],(y1)[ind]),((x1)[(ind+1)%len(x1)],(y1)[(ind+1)%len(x1)])]
        else:
            ind -= len(x1)
            segment1 = [((x2)[ind-1],(y2)[ind-1]),((x2)[ind],(y2)[ind])]
            segment2 = [((x2)[ind],(y2)[ind]),((x2)[(ind+1)%len(y2)],(y2)[(ind+1)%len(y2)])]
            ind += len(x1)
        if not segment1 in segmentlist:
            segmentlist.append(segment1)
            segmentlabels.append(ylabels[ind])
        if not segment2 in segmentlist:
            segmentlist.append(segment2)
            segmentlabels.append(ylabels[ind])
        todelete = []
        for i,segments in enumerate(segmentlist):
            if segments[0][1] > y and segments[1][1] > y:
                todelete.append(i)
        for i in reversed(todelete):
            del segmentlist[i]
            del segmentlabels[i]
        for segment1,l1 in zip(segmentlist[:-1],segmentlabels[:-1]):
            for segment2,l2 in zip(segmentlist[1:],segmentlabels[1:]):
                if not (segment1 == segment2):
                    if not (l1 == l2):
                        result = line_intersect(segment1,segment2)
                        if result['intersect'] == True:
                            if not (result['x_int'],result['y_int']) in intersectlist:
                                intersectlist.append((result['x_int'],result['y_int']))
                                if l1 == 1:
                                    poly1_index = P1.index(segment1[0])
                                    poly2_index = P2.index(segment2[0])
                                else:
                                    poly1_index = P1.index(segment2[0])
                                    poly2_index = P2.index(segment1[0])
                                P1new.insert(poly1_index+1,(result['x_int'],result['y_int']))
                                P2new.insert(poly2_index+1,(result['x_int'],result['y_int']))
                      
    return {'intersectlist':intersectlist, 'P1':P1new, 'P2':P2new}
        
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
        x_int = x1 + (x2-x1)*s
        y_int = y1 + (y2-y1)*s
        intersect = True
    else:
        intersect = False
        x_int = False
        y_int = False
    return {'intersect':intersect, 'x_int':x_int, 'y_int':y_int} 

if __name__ == '__main__':
    polygon_intersect(P1,P2)
