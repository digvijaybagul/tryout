# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:36:29 2015

@author: Shilpa 
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
        #why tc-2 and not tc-1????
        
        #zeros(shape[, dtype, order])	Return a new array of given shape and type, filled with zeros.
        errH=sc.zeros(n)
        errC=sc.zeros(n)
        errH[0]=errHL; errC[0]=errCL
        errH[-1]=errHR; errC[-1]=errCR
        
        errH[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mh*Cp(Th[1:-1])))+((Th[2:]-Th[1:-1])/dA)
        errC[1:-1]=(U*(Th[1:-1]-Tc[1:-1])/(mc*Cp(Tc[1:-1])))+((Tc[2:]-Tc[1:-1])/dA)        
        return sc.concatenate((errH,errC)) #Join a sequence of arrays together.
        
        
f = lambda T: 4184 + 10**(-1)*T + 10**(-3)*T**2 + 10**(-6)*T**3
     
     #f=4.184+(10**-9)*T**3+(10**-6)*T**2+(10**-4)*T
        

#class Fluid(object):
 #   def _init_(self,m,Cp):
        #init is the constructor for a class. The self parameter refers to the instance of the object
    #The init method gets called when memory for the object is allocated:
    #It is important to use the self parameter inside an object's method if you want to persist the value with the object. 
  #      self.m=m
   #     self.Cp=Cp

#fluid1=Fluid(1,f)
#fluid2=Fluid(2,f)  
#assigning for hot and cold fluids
class Fluid(object):
    def __init__(self,m,Cp):
        self.m=m
        self.Cp=Cp
fluid1=Fluid(1,f)   #for hot fluid return function(class) Fluid 
# similarly for cold
fluid2=Fluid(2,f)    

#class InletTemp(object):
 #   def _init_(self,Thin,Tcin):
  #      self.Thin=Thin
   #     self.Tcin=Tcin
    #can be done this way but we wish to reduce no of attributes

#class InletTemp(object):
  #  def _init_(self,Tin):
 #       self.Tin=Tin
#Thin=InletTemp(373.16)
#Tcin=InletTemp(303.16)

class InletTemp(object):
    def __init__(self,Tin):
        self.Tin=Tin
Thin=InletTemp(373.16)
Tcin=InletTemp(303.16)

class DPHE(object):
    def _init_(self,A,U,n):
        self.A=A
        self.U=U
        self.mh=fluid1.m
        self.mc=fluid2.m
        self.Thin=Thin.Tin
        self.Tcin=Tcin.Tin
        self.Cp=fluid1.Cp
        self.Cp=fluid2.Cp
        self.SetGrid(n)
        
        self.solve()
        
    def SetGrid(self,n):
        self.n=n
        self.Th=sc.ones(n)*self.Thin
        self.Tc=sc.ones(n)*self.Tcin
        #Return a new array of given shape and type, filled with ones.
        self.dA=self.A/(n-1)
        self.Tguess=sc.concatenate((self.Th,self.Tc))
        print "n:"
        print self.n
        print self.dA
    #def solve(self):
        #Tguess=self.Tguess
        #soln=opt.leastsq(residuals,Tguess,args=(self))
        #Tsoln=soln[0]
        #self.Thsoln=Tsoln[:self.n]
        #self.Thsoln[0]=self.Thin
        #self.Tcsoln=Tsoln[self.n:]
        #self.Tcsoln[-1]=self.Tcin
        #print self.Thsoln
        #print "Tcsoln: "
        #print self.Tcsoln
        #b=sc.linspace(0,10,10)
        #plt.plot(b,self.Thsoln,'b')
        #plt.show()
        #plt.plot(b,self.Tcsoln,'g')
        #plt.show()
#a = DPHE(10,300,10)

         
         
         
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


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    