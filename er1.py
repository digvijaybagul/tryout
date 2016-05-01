# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 15:27:13 2016

@author: vhd
"""
import win32com.client
import scipy,scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

xl=win32com.client.gencache.EnsureDispatch("Excel.Application")
wb=xl.Workbooks('mydata.xlsx')
sheet=wb.Sheets('Sheet1')
def getdata(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
    
x=getdata(sheet,"A2:A15")
y=getdata(sheet,"B2:B15")    

def curve(x,p):
    [A,B,C]=p
    y=(x+(A*x))*(B)*(C)
    return y
def error(p,x,yexp):
    ycalc=curve(x,p)
    error=ycalc-yexp
    return error
def get_r2(x,y,ycalc):
    ymean=scipy.average(y)
    dymean2=(y-ymean)**2
    dycalc2=(y-ycalc)**2
    r2=1-sum(dycalc2)/sum(dymean2)
    return r2
pguess = [0.02,9.81,1000]
plsq=scipy.optimize.leastsq(error,pguess,args=(x,y))
p=plsq[0]
ycalc=curve(x,p)
r2=get_r2(x,y,ycalc)

fig=plt.figure();ax=fig.add_subplot(111)
ax.plot(x,y,'ro');
ax.plot(x,ycalc,'b')
ax.title.set_text('r2=%f'%(r2))
fig.canvas.draw()    
plt.show()