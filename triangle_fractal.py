# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:37:21 2022

@author: Cristian Finley
"""

import matplotlib.pyplot as plt
import math as math
import random as rand
plt.rcParams['figure.dpi'] = 500

#so first I need to define the vertices of the triangle
#I need to create a number generator for x,y coordinate
#I need to create function that randomly chooses a vertex


#all this does is create a random (x,y) point inside of an equilateral triangle with its base on
#the x-axis with side length 1.  This isn't used here anymore
def createpoint():
    x = rand.uniform(-1,1)
    if x <= 0:
        range1 = x + 1
    if x > 0:
        range1 = -x + 1
    y = rand.uniform(0,range1)
    return(x,y)
    
#This is not actually used, but if you take a point in a triangle and then take the midpoint
#between that point and any random vertex and plot this a bunch of times, you'll get an image
#of the three  triangles that make up the larger triangle.  This is a little bit wierd and 
#I changed my method, but it is still a cool concept
def randmidpoint(x,y):
    x1,y1 = 0,1
    x2,y2 = 1,0
    x3,y3 = -1,0
    
    p = rand.randint(0,2)
    if p == 0:
        x = (x+x1)/2
        y = (y+y1)/2
    if p == 1:
        x = (x+x2)/2
        y = (y+y2)/2
    if p == 2:
        x = (x+x3)/2
        y = (y+y3)/2
    xvals.append(x)
    yvals.append(y)


#this function returns the vertices of 3 triangles within an inputted larger triangle
#This could be easily modified to return 4 triangles or possible even to take other shapes
def subtriangles_3(x1,y1,x2,y2,x3,y3):
    x4,y4 = ((x1+x2)/2),((y1+y2)/2)
    x5,y5 = ((x1+x3)/2),((y1+y3)/2)
    x6,y6 = ((x3+x2)/2),((y3+y2)/2)
    trianglevertices.append([[x1,y1],[x4,y4],[x5,y5],[x1,y1]])
    trianglevertices.append([[x4,y4],[x2,y2],[x6,y6],[x4,y4]])
    trianglevertices.append([[x5,y5],[x6,y6],[x3,y3],[x3,y3]])
    
    
    
    
#This defines the vertices of the original triangle, theoretically this will 
#work with any triangle, it doesn't have to be equilateral
trianglevertices = [[[-1,0],[0,1],[1,0],[-1,0]]]




#this range indicates the number of "layers" of triangles to be made
for i in range(7):
    for i in trianglevertices[:]:
        subtriangles_3(i[0][0],i[0][1],i[1][0],i[1][1],i[2][0],i[2][1])





#this is just taking the vertices of the triangles and adding them to a list of x and y values
#so that they can be plotted.  It is possible that the plot function could handel them in 
#list for but I thought this would be safer
xvals = []
yvals = []
# print(trianglevertices)
for i in trianglevertices:
    for k in i:
        xvals.append(k[0])
        yvals.append(k[1])
plt.axis('off')
plt.plot(xvals,yvals,linewidth=0.4,c='black')













