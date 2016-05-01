# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 03:19:28 2015

@author: R014Tx
"""

import scipy as sc
import matplotlib.pyplot as plt
import scipy.optimize as opt
def residuals(T,obj):
        n=obj.n
        Thin=obj.Thin
        Tcin=obj.Tcin
        Th=T[n:]
        Tc=T[:n]
        dA=obj.dA
        U=obj.U
        mh=obj.mh
        mc=obj.mc
        Cp=obj.Cp
        errHL=(U*(Thin-Tc[0])/(mh*Cp(Thin)))+((-Thin+Th[1])/dA)
        errCL=(U*(Thin-Tc[0])/(mc*Cp(Tc[0])))+((Tc[1]-Tc[0])/dA)        
        errHR=(U*(Th[-1]-Tcin)/(mh*Cp(Th[-1])))+((Th[-1]-Th[-2])/dA)
        errCR=(U*(Th[-1]-Tcin)/(mc*Cp(Tcin)))+((Tcin-Tc[-2])/dA)
        errH=sc.zeros(n)
        errC=sc.zeros(n)
        errH[0]=errHL; errC[0]=errCL
        errH[-1]=errHR; errC[-1]=errCR
        
        errH[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mh*Cp(Th[1:-1])))+((Th[2:]-Th[1:-1])/dA)
        errC[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mc*Cp(Tc[1:-1])))+((Tc[2:]-Tc[1:-1])/dA)        
        return sc.concatenate((errH,errC))
        
f = lambda T: 4184 + 10**(-1)*T + 10**(-3)*T**2 + 10**(-6)*T**3
class DPHE(object):
    def __init__(self,A,U,mh,mc,Thin,Tcin,n,Cp):
        self.A=A
        self.U=U
        self.Cp=Cp
        self.set_hex(mh,mc,Thin,Tcin)
        self.set_grid(n)
    
        self.solve()
    def set_hex(self,mh,mc,Thin,Tcin):
        self.mh=mh
        self.mc=mc
        self.Thin=Thin
        self.Tcin=Tcin
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

a = DPHE(10,300,1,2,373.16,303.16,10,f)
