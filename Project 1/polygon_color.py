#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import readfile
import sys

poly = [(21,21),(15,42),(12,42),(6,30),(3,18),(3,9),(15,9)]
i = 0;

def polygon_color(file):

# Read in input file and arrange points in desired format
    result = readfile.readfile(file)
    poly = result['poly1']   
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    
# Sort the x and y coordinates    
    x_sorted = np.sort(px)
    y_sorted = np.sort(py) 
    
# Call functions and plot
    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    colors = plot_boundary(poly)
    flood_fill(int(np.median(px)),int(np.median(py)), 'w', 'g', x_sorted[0], y_sorted[0], colors)   
    plt.show(block=False)

# This function creates a 'colors' map that holds the index and 
# color of each point in/near the polygon. Everything is initialized to white
def plot_boundary(poly):
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    x_sorted = np.sort(px)
    y_sorted = np.sort(py)
    colors = [['w' for x in range(y_sorted[-1] - y_sorted[0] + 1)] for x in range(x_sorted[-1] - x_sorted[0] + 1)] 
    colors = plot_poly(px,py,colors,x_sorted[0],y_sorted[0])
    return colors

# This function uses the flood-fill algorithm to recursively color the polygon.
# The boundary condition uses the color map and checks what color neighboring points are  
def flood_fill(x, y, OldColor, NewColor, xmin, ymin, colors):
    if (colors[x - xmin][y - ymin] == OldColor):  
        if (i < 100):    
            plt.plot(x, y, marker='.', markersize = 15, markerfacecolor = 'g')
            colors[x-xmin][y-ymin] = NewColor
            flood_fill(x,y-1,OldColor, NewColor, xmin, ymin, colors)
            flood_fill(x,y+1,OldColor, NewColor, xmin, ymin, colors)
            flood_fill(x-1,y,OldColor, NewColor, xmin, ymin, colors)
            flood_fill(x+1,y,OldColor, NewColor, xmin, ymin, colors)

# This function steps through the segements of a polygon in a counterclockwise
# direction and calls the plot_line function with the segment's lower y-coord
# as the first input 
def plot_poly(px, py, colors,xmin,ymin):
    for i in range(len(px)):
        p1 = (px[i], py[i])
        p2 = (px[(i+1)%len(px)],py[(i+1)%len(px)])
        if (p1[0] <= p2[0]):
            colors = plot_line(p1,p2,colors,xmin,ymin)
        else:
            colors = plot_line(p2,p1,colors,xmin,ymin)
    return colors

# This function uses the Bresenham algorithm to plot a line, and sets the index 
# of each point on the line in the color map to magenta
def plot_line(p1,p2,colors,xmin,ymin):
    marker_size = 15
    vertical = False
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
# Find the slope and y-intercept ie formula for the line
    if (x2-x1) != 0:
        slope = float(y2-y1)/(x2-x1)
        b = float(y2 - slope*x2)
    else:
        vertical = True
    xval = x_plot = x1
    yval = y_plot = y1
    plt.plot(xval, y_plot, marker='.', markersize = marker_size, markerfacecolor = 'm')
    colors[xval - xmin][y_plot - ymin] = 'm'
    if vertical != True:
# Plot a horizontal line
        if (slope == 0):
            for i in range (x2 - x1):
                xval += 1
                plt.plot(xval, y_plot, marker='.', markersize = marker_size, markerfacecolor = 'm')
                colors[xval - xmin][y_plot - ymin] = 'm'
# Based on slope and positive vs negative, increment coordinates according to midpoint
        elif (slope > 0):
            if (slope <= 1):
                for i in range(x2-x1):
                    xval += 1
                    yval = float(slope*xval + b)
                    midpoint = y_plot + .5
                    if yval > midpoint:
                        y_plot += 1
                    plt.plot(xval, y_plot, marker='.', markersize = marker_size, markerfacecolor = 'm')
                    colors[xval - xmin][y_plot - ymin] = 'm'
            else:
                for i in range(y2-y1):
                    yval += 1
                    xval = float((yval-b)/slope)
                    midpoint = x_plot + .5
                    if xval > midpoint:
                        x_plot += 1
                    plt.plot(x_plot, yval, marker='.', markersize = marker_size, markerfacecolor = 'm')
                    colors[x_plot - xmin][yval - ymin] = 'm'
        else:
            if (slope >= -1):
                for i in range(x2-x1):
                    xval += 1
                    yval = float(slope*xval + b)
                    midpoint = y_plot - .5
                    if yval < midpoint:
                        y_plot -= 1
                    plt.plot(xval, y_plot, marker='.', markersize = marker_size, markerfacecolor = 'm')
                    colors[xval - xmin][y_plot - ymin] = 'm'
            else:
                for i in range(y1 - y2):
                    yval -= 1
                    xval = float((yval-b)/slope)
                    midpoint = x_plot + .5
                    if xval > midpoint:
                        x_plot += 1
                    plt.plot(x_plot, yval, marker='.', markersize = marker_size, markerfacecolor = 'm')
                    colors[x_plot - xmin][yval - ymin] = 'm'
    else:
# Plot a vertical line
        for i in range (y1- y2):
            yval -= 1
            plt.plot(x_plot, yval, marker='.', markersize = marker_size, markerfacecolor = 'm')
            colors[x_plot - xmin][yval - ymin] = 'm'
    return colors        


#if __name__ == '__main__':
#    polygon_color(poly)
