# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:49:31 2022

@author: Cristian Finley
"""

#Ok, I need to lay out some initial things to do
#   1. Create a function to generate complex numbers
#       a. first generate x-values between -2 and 2
#       b. then generate y-values, but how? randomly? no, the same amount as count?
#   2. create a function to square each point
#   (a+bi)(a+bi) = a^2 - b^2 + 2*a*b
#   3. Create a function to iterate on those numbers
#
#   4. Plot points that are stable/unstable as different colors
#   optional: create a function to determine how many different colors are plotted

import matplotlib.pyplot as plt
import math as math

def plotrange():
    x = input('Domain "x1,x2": ').strip().split(",")
    y = input('Domain "y1,y2": ').strip().split(",")
    return(float(x[0]),float(x[1]),float(y[0]),float(y[1]))
    


def complexnumber(x1,x2,y1,y2,count):
    count = count
    xvals=[]
    yvals=[]
    xrange = x2-x1
    yrange = y2-y1
    for i in range(count+1):
        xincrement = xrange/count
        yincrement = yrange/count
        print(xincrement*i+x1)
        xvals.append(xincrement*i+x1)
        #xvals.append(-xincrement*i+x2)
        yvals.append(yincrement*i+y1)
        #yvals.append(-yincrement*i+y2)
    return(xvals,yvals)

    
def square(xval,yval):
    return (xval**2-yval**2,2*xval*yval)

def iterate(a, b, i, j):
    a, b = (a**2-b**2 + i, 2*a*b + j)
    return (a, b)

def outsidecircle(xvals, yvals):
    outside = []
    global colors
    colors = []

    for i in xvals:
        #print(i)
        print(xvals.index(i))
        for j in yvals:
            counter = 0
            a = i
            b = j
            while counter < 100:
                if a**2 + b**2 > 2:
                    #print(counter)
                    #print(i,j)
                    outside.append([i,j])
                    colors.append(counter)
                    break
                if -0.001 < a < 0.001 and -0.001 < b < 0.001 :
                    break
                a,b = iterate(a,b,i,j)
                counter += 1
    return outside
   
 
    
   
########################### main code ########################################  
x1,x2,y1,y2 = -1.5,0.5,-1,1
#input desired bounds here ^^

#creates grid of points to check based on input bouds of graph        
xvals,yvals = complexnumber(x1,x2,y1,y2,300)


#determines whether the point should be plotted based on if it converges or diverges
outside = outsidecircle(xvals,yvals)
xvals = []
yvals = []

#recreates xvals and yval, nothing important here
for i in outside:  
    xvals += [i[0]]
    yvals += [i[1]]

#this reverse the colors, comment out if you don't want that
for x,i in enumerate(colors):
      colors[x] =(i)

plt.xlim(x1,x2)
plt.ylim(y1,y2)
plt.scatter(xvals,yvals,s=1,c='blue')





#RANGES
#full view (-1.5,0.5,-1,1)
#smaller circle (-1.5,-1.25,-.15,.10)
#seahorse valley (-0.8,-.70,0.1,0.2)
#microseahorse valley (-0.75,-0.73,0.14,0.16)
#nanoseahorse valley (-0.7450,-0.7425,.1425,.1450)

#COLORMAPS
#cividis
#magma
#inferno
#plasma
#viridis
#twilight_shifted