# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 03:38:23 2015

@author: R014Tx
"""


import scipy as sc
import matplotlib.pyplot as plt
import scipy.optimize as opt

def residuals(T,obj):    
    n=obj.n 
    Thin=obj.Thin
    Tcin=obj.Tcin
    Th=T[:n]
    Tc=T[n:]
    dA=obj.dA
    U=obj.U
    mh=obj.mh
    mc=obj.mc
    Cp=obj.Cp
    errHL=(U*(Thin-Tc[0])/(mh*Cp(Thin)))+((Th[1]-Thin)/dA)

    errCL=(U*(Thin-Tc[0])/(mc*Cp(Tc[0])))+((Tc[1]-Tc[0])/dA)

    errHR=(U*(Th[-1]-Tcin)/(mh*Cp(Th[-1])))+((Th[-1]-Th[-2])/dA)
    errCR=(U*(Th[-1]-Tcin)/(mc*Cp(Tcin)))+((Tcin-Tc[-2])/dA)

     
    errH=sc.zeros(n) 
    errC=sc.zeros(n)


    errH[0]=errHL; errH[-1]=errHR 

    errC[0]=errCL;errC[-1]=errCR

    errH[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mh*Cp(Th[1:-1])))+((Th[2:])-Th[1:-1])/dA

    errC[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mc*Cp(Tc[1:-1])))+((Tc[2:])-Tc[1:-1])/dA
  
    return sc.concatenate((errH,errC))
   
   
f = lambda T: 4184 + 10**(-1)*T + 10**(-3)*T**2 + 10**(-6)*T**3
class Fluid(object):
    def __init__(self,m,Cp):
        self.m=m
        self.Cp=Cp
fluid1=Fluid(1,f)  
fluid2=Fluid(2,f)    
    
class InletTemp(object):
    def __init__(self,Tin):
        self.Tin=Tin
Thin=InletTemp(373.16)
Tcin=InletTemp(303.16)
    
class DPHE(object):
    def __init__(self,A,U,n):
        self.A=A
        self.U=U
        self.mh=fluid1.m 
        self.mc=fluid2.m
        self.Thin=Thin.Tin
        self.Tcin=Tcin.Tin
        self.Cp=fluid1.Cp
        self.Cp=fluid2.Cp
        self.set_grid(n)
    
        self.solve()
    def set_grid(self,n):
        self.n=n
        self.Th=sc.ones(n)*self.Thin
        self.Tc=sc.ones(n)*self.Tcin
        self.dA=self.A/(n-1)
        self.Tguess=sc.concatenate((self.Th,self.Tc))
        print "n:"
        print self.n
        print self.dA
        
    
    def solve(self):
        Tguess=self.Tguess
        soln=opt.leastsq(residuals,Tguess,args=(self))
#all the attributes of self are available for this function solve
        Tsoln=soln[0]
        self.Thsoln=Tsoln[:self.n]
        self.Thsoln[0]=self.Thin
        self.Tcsoln=Tsoln[self.n:]
        self.Tcsoln[-1]=self.Tcin
        print "Thsoln: "
        print self.Thsoln
        print "Tcsoln: "
        print self.Tcsoln
        b=sc.linspace(0,10,10)
        plt.plot(b,self.Thsoln,'r')
        plt.show()
        plt.plot(b,self.Tcsoln,'b')
        plt.show()
a = DPHE(10,300,10)