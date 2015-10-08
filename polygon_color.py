#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def polygon_color():
    px = (21, 15, 12,  6,  3, 3, 15)
    py = (21, 42, 42, 30, 18, 9, 9)
    plt.cla()
    plot_poly(px,py)
    plt.axis('equal')

   # plt.plot(px,py)
   # plt.show()

def plot_poly(px, py):
    for i in range(len(px)):
        p1 = (px[i], py[i])
        p2 = (px[(i+1)%len(px)],py[(i+1)%len(px)])
        if (p1[0] <= p2[0]):
            plot_line(p1,p2)
        else:
            plot_line(p2,p1)

def plot_line(p1,p2):
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
    plt.plot(xval, y_plot, marker='.', markersize = 25)
    if vertical != True:
        if (slope == 0):
            for i in range (x2 - x1):
                xval += 1
                plt.plot(xval, y_plot, marker='.', markersize = 25)
        elif (slope > 0):
            if (slope <= 1):
                for i in range(x2-x1):
                    xval += 1
                    yval = float(slope*xval + b)
                    midpoint = y_plot + .5
                    if yval > midpoint:
                        y_plot += 1
                    plt.plot(xval, y_plot, marker='.', markersize = 25)
            else:
                for i in range(y2-y1):
                    yval += 1
                    xval = float((yval-b)/slope)
                    midpoint = x_plot + .5
                    if xval > midpoint:
                        x_plot += 1
                    plt.plot(x_plot, yval, marker='.', markersize = 25)
        else:
            if (slope >= -1):
                for i in range(x2-x1):
                    xval += 1
                    yval = float(slope*xval + b)
                    midpoint = y_plot - .5
                    if yval < midpoint:
                        y_plot -= 1
                    plt.plot(xval, y_plot, marker='.', markersize = 25)
            else:
                for i in range(y1 - y2):
                    yval -= 1
                    xval = float((yval-b)/slope)
                    midpoint = x_plot + .5
                    if xval > midpoint:
                        x_plot += 1
                    plt.plot(x_plot, yval, marker='.', markersize = 25)
    else:
        for i in range (y1- y2):
            yval -= 1
            plt.plot(x_plot, yval, marker='.', markersize = 25)
    plt.show()
    plt.plot((p1[0], p2[0]),(p1[1], p2[1]))


if __name__ == '__main__':
    polygon_color()
