#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def polygon_color():
    px = (7, 5, 4, 2, 1, 1, 5) #(21, 15, 12,  6,  3, 3, 15)
    py = (7, 14, 14, 10,  6,  3,  3) #(21, 42, 42, 30, 18, 9, 9)
    x_sorted = np.sort(px) # replace!!!
    y_sorted = np.sort(py) # replace!!!
    plt.cla()
    plt.axis('equal')
    colors = [['w' for x in range(y_sorted[-1] - y_sorted[0] + 1)] for x in range(x_sorted[-1] - x_sorted[0] + 1)] 
    colors = plot_poly(px,py,colors,x_sorted[0],y_sorted[0])
    print colors
    flood_fill(int(np.median(px)),int(np.median(py)), 'w', 'g', x_sorted[0], y_sorted[0], colors) # replace!!!

def flood_fill(x, y, OldColor, NewColor, xmin, ymin, colors):
 #   if(x >= 0 && x < w && y >= 0 && y < h && screenBuffer[x][y] == oldColor && screenBuffer[x][y] != newColor) 

    if (colors[x - xmin][y - ymin] == OldColor and colors[x-xmin+1][y-ymin] != 'm' and colors[x-xmin-1][y-ymin] !='m' and colors[x-xmin][y-ymin-1] != 'm' and colors[x-xmin][y-ymin+1] != 'm'):     
        plt.plot(x, y, marker='.', markersize = 15, markerfacecolor = 'g')
        colors[x-xmin][y-ymin] = NewColor
        flood_fill(x,y-1,OldColor, NewColor, xmin, ymin, colors)
        print('here1')
        print(x)
        print(y)
        print(NewColor)
        flood_fill(x,y+1,OldColor, NewColor, xmin, ymin, colors)
        print('here2')
        print(x)
        print(y)
        print(NewColor)
        flood_fill(x-1,y,OldColor, NewColor, xmin, ymin, colors)
        print('here3')
        print(x)
        print(y)
        print(NewColor)
        flood_fill(x+1,y,OldColor, NewColor, xmin, ymin, colors)
        print('here4')
        print(x)
        print(y)
        print(NewColor)


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
        b = float(y2 - slope*x2) # y-intercept
    else:
        vertical = True
    xval = x_plot = x1
    yval = y_plot = y1
    plt.hold(True)
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
    plt.show()
    return colors
    #plt.plot((p1[0], p2[0]),(p1[1], p2[1]))


if __name__ == '__main__':
    polygon_color()
