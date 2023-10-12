# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:14:34 2022

@author: Cristian Finley
"""

import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 500



#alright, so...I need to create a graph that plots the path that a constand takes for
#kaprekars constant to get to the special value.  To do this, I need to use some of my
#old code and make a set of data points that 

#for i in numbers 1-10000
    #follow the path and plot the line



        
        




def createinput(num):
    list1 = []
    if int(num)<1000:
        list1.append(0)
    if int(num)<100:
        list1.append(0)
    if int(num)<10:
        list1.append(0)
    
    for i in str(num):
        list1.append(int(i))
    return list1


def sortnumber(list1):
    list1.sort()
    list2 = list1[:]
    list2.sort(reverse=True)
    num1 = ''
    num2 = ''
    
    for i in list1:
        num1 = num1+str(i)
    
    for i in list2:
        num2 = num2+str(i)
        
    num2 = int(num2)
    num1 = int(num1)
    return (num1,num2)

def subtraction(num1,num2):

    if num2>num1:
        num3 = num2 - num1    
    else:
        num3 = num1 - num2
        
    return num3
    
xvals = []  
three = [] 
for u in range(1,10000):
    count = 0
    i = u
    if i == 6174:
        continue
    while i != 6174:
        print(i)
        list1 = createinput(i)
        num1,num2 = sortnumber(list1)
        if num1 - num2 == 0: 
            break
        i = subtraction(num1,num2)
        count += 1
    if count ==3:
        three.append(u)
    xvals.append(count)
print(three)
plt.hist(xvals,linewidth = .4,bins=[0,1,2,3,4,5,6,7],color = 'blue',histtype='bar',alpha = .75) 