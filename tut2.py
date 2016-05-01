# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 11:15:19 2015

@author: vhd
"""

import scipy
from matplotlib import pyplot as plt
def f1(x):
    return scipy.cos(x)
def f2(x):
    return scipy.cos(2*x)
f3=lambda x:scipy.cos(3*x)
f4=lambda x:scipy.cos(4*x)
listf=[f1,f2,f3,f4]
x=scipy.linspace(0,2*scipy.pi,1000)
fig=plt.figure()
ax1=fig.add_subplot(211);fig.show()
ax2=fig.add_subplot(212);fig.show()
for f in listf:
    y=f(x)
    ax1.clear()
    ax1.plot(x,y,'r')
    ax2.clear()
    ax2.plot(x,y,'r')
    plt.pause(0.1)
    