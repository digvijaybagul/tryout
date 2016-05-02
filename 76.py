# -*- coding: utf-8 -*-
"""
Created on Mon May 02 12:30:47 2016

@author: vhd
"""

import numpy as np
import scipy
from scipy.optimize import leastsq
import win32com.client


xl= win32com.client.gencache.EnsureDispatch('Excel.Application')
wb=xl.Workbooks('ExamProblemData2.1.xlsx')
sheet=wb.Sheets('ExamProblemData')
   
def getdata(sheet, Range):
    data= sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
tdata=getdata(sheet,"A2:A11")
cadata=getdata(sheet,"B2:B11")
cddata=getdata(sheet,"C2:C11")
ccdata=getdata(sheet,"F2:F11")
cbdata=getdata(sheet,"G2:G11")
yddata=getdata(sheet,"D2:D11")
yadata=getdata(sheet,"F2:F11")

#for T=250K
def assign(ca,cc, p):
    k2= p
    return (k2*ca*cc)
    
def residuals(p, yd,cc, ca):
    k2 = p
    err = (yd-(k2*ca*cc))
    return err
    
def assign1(ca,cb,cc, q):
    k1,k2= q
    return (k1*ca*cb+k2*ca*cc) 
    
def residuals1(q, ya,ca,cb, cc):
    k1,k2,k3 = q
    err1 = (ya+(k2*ca*cc+k1*ca*cb))
    err2= (k1*ca*cb+k3*cb*cb-50)
    return err1
    return err2


guessk2=[1]
fitting = leastsq(residuals, guessk2, args=(yddata,ccdata, cadata))
popt=fitting[0]
pcov=fitting[1]
print("*******************************")
print("Optimized k2")
print popt[0]

guessk=[1,1,1]
fitting = leastsq(residuals1, guessk, args=(yadata,cadata, cbdata,ccdata))
popt=fitting[0]
pcov=fitting[1]
print("*******************************")
print("Optimized k2")
print popt[0],popt[1],popt[2]

#for T=350K
#for T=400K
#for Arhenius k01,k02,k03
"""lnk1/k11= -E*((1/250)-(1/300))/R
"""

#dnadt=-k1*CaC