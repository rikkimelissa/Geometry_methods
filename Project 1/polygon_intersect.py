#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from polygon_color import plot_boundary # how to import?
from polygon_color import flood_fill
import readfile

P1 = [(21,21),(15,42),(12,42),(6,30),(3,18),(3,9),(15,9)]
P2 = [(15,24),(27,30),(15,51),(12,33)]
file = 'Input 2.txt'

def polygon_intersect(file):

# Read the input file in the correct format. Use the plot_boundary function
# to plot the polygons
    result = readfile.readfile(file)
    P1 = result['poly1']
    P2 = result['poly2']
    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    plot_boundary(P2)
    plot_boundary(P1)

# Find the intersections of the polygons and compose the new polygon
    result = find_intersections(P1,P2)
    P3 = compose_new_polygon(result)
    P3 = [[int(float(j)) for j in i] for i in P3]
 
# Use the plot_boundary and flood_fill functions to plot the new polygon   
    poly = P3
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    x_sorted = np.sort(px) # replace!!!
    y_sorted = np.sort(py) # replace!!!
    colors = plot_boundary(poly)
    plt.plot(int(np.median(px)),int(np.median(py)), marker='.', markersize = 15, markerfacecolor = 'g')
    flood_fill(int(np.median(px)),int(np.median(py)), 'w', 'g', x_sorted[0], y_sorted[0], colors)
    plt.show(block=False)

# The input for this function is the two polygons with the intersections points
# as vertices and the list of intersections
def compose_new_polygon(result):
    P1 = result['P1']
    P2 = result['P2']
    P3 = []
    intersect_list = result['intersectlist']
    p1_index0 = P1.index(intersect_list[0])
    p2_index0 = P2.index(intersect_list[0])
    p1_index1 = P1.index(intersect_list[1])
    p2_index1 = P2.index(intersect_list[1])
# Pick an intersection point and find which direction will be counter clockwise
    seg1 = [a - b for a,b in zip(P1[p1_index0 + 1], intersect_list[0])]
    seg2 = [a - b for a,b in zip(intersect_list[0], P2[p2_index0 + 1])]
    tri_dir = np.cross(seg1,seg2)
# Step through the new polygon, starting at an intersection point and following
# one polygon around until it hits the second intersection point, then follow the
# other polygon until back at the first intersection point
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

# This function uses a sweep line to find all intersection points between
# the two polygons
def find_intersections(P1,P2):
    x1 = [P1[i][0] for i in range(len(P1))]
    y1 = [P1[i][1] for i in range(len(P1))]
    x2 = [P2[i][0] for i in range(len(P2))]
    y2 = [P2[i][1] for i in range(len(P2))]
# Sort the y-coordinates and create an event list
    ylist = np.sort(y1 + y2)
    eventlist = ylist[::-1]
# Label y values according to polygon and find the order of the event list
    ylabels = [1]*len(y1) + [2]*len(y2)
    ylist_ind = np.argsort(y1 + y2)
    order = ylist_ind[::-1]
# Initialize empty arrays
    segmentlist = []
    segmentlabels = []
    intersectlist = []
    P1new = P1
    P2new = P2
# Step through event list
    for y, ind in zip(eventlist,order):
# Find previous and next segments according to label of event (y--coord)
        if (ylabels[ind] == 1):
            segment1 = [((x1)[ind-1],(y1)[ind-1]),((x1)[ind],(y1)[ind])]
            segment2 = [((x1)[ind],(y1)[ind]),((x1)[(ind+1)%len(x1)],(y1)[(ind+1)%len(x1)])]
        else:
            ind -= len(x1)
            segment1 = [((x2)[ind-1],(y2)[ind-1]),((x2)[ind],(y2)[ind])]
            segment2 = [((x2)[ind],(y2)[ind]),((x2)[(ind+1)%len(y2)],(y2)[(ind+1)%len(y2)])]
            ind += len(x1)
# If either segment is new (ie y-coord is upper endpoint), add it to the current
# segment list (segements on the segementlist get tested for intersections)
        if not segment1 in segmentlist:
            segmentlist.append(segment1)
            segmentlabels.append(ylabels[ind])
        if not segment2 in segmentlist:
            segmentlist.append(segment2)
            segmentlabels.append(ylabels[ind])
        todelete = []
# If any segment in the segment list is now above the sweep line, delete it
        for i,segments in enumerate(segmentlist):
            if segments[0][1] > y and segments[1][1] > y:
                todelete.append(i)
        for i in reversed(todelete):
            del segmentlist[i]
            del segmentlabels[i]
# Test segments in segment list for intersections
        for segment1,l1 in zip(segmentlist[:-1],segmentlabels[:-1]):
            for segment2,l2 in zip(segmentlist[1:],segmentlabels[1:]):
# Check that the segment isn't being tested against itself or any other segment
# classified in the same polygon
                if not (segment1 == segment2):
                    if not (l1 == l2):
# Test for intersection
                        result = line_intersect(segment1,segment2)
                        if result['intersect'] == True:
# If the result is true, add it to the intersectlist and as a vertex in the polygon
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

# This function finds the intersection between two line segements if it exists      
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

#if __name__ == '__main__':
#    polygon_intersect(file)
