#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def polygon_color():
    px = (7,5,4,2,1,5)
    py = (7,14,14,10,6,3)

   # plt.plot(px,py)
   # plt.show()

def plot_line(p1,p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    slope = float(y2-y1)/(x2-x1)
    b = float(y2 - slope*x2) # y-intercept
    xval = x_plot = x1
    yval = y_plot = y1
    plt.hold(True)
    plt.plot(xval, y_plot, marker='.', markersize = 25)
    if (slope > 0):
        if (slope <= 1):
            for i in range(x2-x1):
                xval += 1
                yval = slope*xval + b
                midpoint = y_plot + .5
                if yval > midpoint:
                    y_plot += 1
                plt.plot(xval, y_plot, marker='.', markersize = 25)
        else:
            for i in range(y2-y1)
    plt.show()
    plt.plot((p1[0], p2[0]),(p1[1], p2[1]))


if __name__ == '__main__':
    polygon_color()
