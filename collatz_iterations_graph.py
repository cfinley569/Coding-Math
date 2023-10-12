# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:41:11 2022

@author: Cristian Finley
"""
import time

start = time.time()

import matplotlib.pyplot as plt


n = 100
plotline = []
    
    
for i in range(2,1000000):
    counter = 0
    if i == 1:
        continue
   
    while int(i) != 1:
        if i%2 == 0:
            i = i/2
        else:
            i = 3*i +1
        counter += 1
    print(counter)
    plotline.append(counter)
    
plt.xlabel("Total Iterations")
plt.hist(plotline,bins='auto',alpha=0.75)   

end = time.time()
print(end-start)
    
































