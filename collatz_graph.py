# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:41:11 2022

@author: Cristian Finley
"""

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 500



#alright, so...I need to create a graph that plots the path that a constand takes for
#kaprekars constant to get to the special value.  To do this, I need to use some of my
#old code and make a set of data points that 

#for i in numbers 1-10000
    #follow the path and plot the line

    
    
for i in range(1,11):
    print(i)
    if i == 1:
        continue
    xvals = [0,1,2,3,4,5,6,7]
    plotline = []
    plotline.append(i)
    while int(i) != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = 3*i +1
        plotline.append(i)
    
    
    while len(plotline) < len(xvals):
        xvals.pop()
    while len(xvals) < len(plotline):
        xvals.append(xvals[-1]+1)
    plt.plot(xvals,plotline,linewidth = .4,linestyle = 'solid',color='black',alpha = .5)   

    
    
































