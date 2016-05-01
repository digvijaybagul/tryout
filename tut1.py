# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 12:14:00 2015

@author: vhd
"""

print 'Hello'
import os
print os.getcwd()
x=3
if x>2:
    print "x greater than 2"
    print "xx xx"
elif x<4:
    print "x more than 2 but less than 4"
else:
    print x
y=[1,3,'cat',4.0,True,83.67]
for x in y:
    print x    
x=range(0,30);y=[xx**2 for xx in x]
import pylab
pylab.plot(x,y,'r')
pylab.show()

