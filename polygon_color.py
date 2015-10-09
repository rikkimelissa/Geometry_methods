#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

poly = [(21,21),(15,42),(12,42),(6,30),(3,18),(3,9),(15,9)]

def polygon_color(poly):
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    x_sorted = np.sort(px) # replace!!!
    y_sorted = np.sort(py) # replace!!!
    plt.cla()
    plt.axis('equal')
    plt.grid('on')
    plt.hold(True)
    colors = plot_boundary(poly)
    flood_fill(int(np.median(px)),int(np.median(py)), 'w', 'g', x_sorted[0], y_sorted[0], colors)   
    plt.show(block=False)

def plot_boundary(poly):
    px = [poly[i][0] for i in range(len(poly))]
    py = [poly[i][1] for i in range(len(poly))]
    x_sorted = np.sort(px) # replace!!!
    y_sorted = np.sort(py) # replace!!!
    colors = [['w' for x in range(y_sorted[-1] - y_sorted[0] + 1)] for x in range(x_sorted[-1] - x_sorted[0] + 1)] 
    colors = plot_poly(px,py,colors,x_sorted[0],y_sorted[0])
    return colors
    
def flood_fill(x, y, OldColor, NewColor, xmin, ymin, colors):
    if (colors[x - xmin][y - ymin] == OldColor):      
        plt.plot(x, y, marker='.', markersize = 15, markerfacecolor = 'g')
        colors[x-xmin][y-ymin] = NewColor
        flood_fill(x,y-1,OldColor, NewColor, xmin, ymin, colors)
        flood_fill(x,y+1,OldColor, NewColor, xmin, ymin, colors)
        flood_fill(x-1,y,OldColor, NewColor, xmin, ymin, colors)
        flood_fill(x+1,y,OldColor, NewColor, xmin, ymin, colors)

def plot_poly(px, py, colors,xmin,ymin):
    for i in range(len(px)):
        p1 = (px[i], py[i])
        p2 = (px[(i+1)%len(px)],py[(i+1)%len(px)])
        if (p1[0] <= p2[0]):
            colors = plot_line(p1,p2,colors,xmin,ymin)
        else:
            colors = plot_line(p2,p1,colors,xmin,ymin)
    return colors

def plot_line(p1,p2,colors,xmin,ymin):
    marker_size = 15
    vertical = False
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
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
        if (slope == 0):
            for i in range (x2 - x1):
                xval += 1
                plt.plot(xval, y_plot, marker='.', markersize = marker_size, markerfacecolor = 'm')
                colors[xval - xmin][y_plot - ymin] = 'm'
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
        for i in range (y1- y2):
            yval -= 1
            plt.plot(x_plot, yval, marker='.', markersize = marker_size, markerfacecolor = 'm')
            colors[x_plot - xmin][yval - ymin] = 'm'
    return colors        


if __name__ == '__main__':
    polygon_color(poly)
