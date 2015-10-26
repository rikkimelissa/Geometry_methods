#!/usr/bin/env python

import csv

def readfile(file):
    f = open(file,'rt')
    poly1 = []
    poly2 = []
    points = []
    poly_list = []     
    try:
        reader = csv.reader(f) #, dialect=csv.Dialect.lineterminator)
        for row in reader:
            poly_list.append(row)
    finally:
        x = 1
        print(poly_list)
        if (poly_list[0][0] == 'P'):
            list_type = 0
        if (poly_list[0][0] == 'U'):
            list_type = 1
        if (poly_list[0][0] == 'S'):
            list_type = 2       
        del poly_list[0]
    if (list_type == 0):
        for row in poly_list:
            x = int((row[0].split('('))[1])
            y = int((row[1].split(')'))[0])
            poly1.append((x,y))
    if (list_type == 2):
        for row in poly_list:
            x = int((row[0].split('('))[1])
            y = int((row[1].split(')'))[0])
            points.append((x,y))
    if (list_type == 1):
        del poly_list[0]
        p2_index = poly_list.index(['P2'])
        del poly_list[p2_index]
        for row in poly_list[0:p2_index]:
            x = int((row[0].split('('))[1])
            y = int((row[1].split(')'))[0])
            poly1.append((x,y))
        for row in poly_list[p2_index:]:
            x = int((row[0].split('('))[1])
            y = int((row[1].split(')'))[0])
            poly2.append((x,y))
    return {'poly1':poly1, 'poly2':poly2, 'points':points}
    
if __name__ == '__main__':
    result = readfile(file)

