# -*- coding: utf-8 -*-
import scipy
from scipy import linspace
from matplotlib.pyplot import plot,pause,show

A=0.2 # Area of slab m^2
L=10.0 # length of slab m 
n=100 # no. of parts
Ts=25.0 # surronding temperature
T=scipy.ones(100)*Ts
T[0]=200 
T[1]=200
t=0
p=7000
Cp=0.39 # specific heat of substance
P=1.0 # Perimeter of slab 
h=45 # heat transfer coefficient
dt=0.1
dz=L/100.0
ks=50.0 # specific heat conductivity of solid 
kl=2.0 # specific heat conductivity of liquid
def x(T):
    if T<130.0:
        m=0
    if T>150.0:
        m=1.0
    if T<150.0:
        if T>130.0:
            m=(T-130.0)/20.0
    return m
def k(x):
    k=kl*x+(1-x)*ks
    return k
l=linspace(0,L,100)
while t<10:
    for i in range(1,99):
        
        T[i+1]=T[i]+k(x(T[i]))*dt/p/Cp*(T[i+1]-2*T[i]+T[i-1])/dz/dz-h*P/A/p/Cp*dt*(T[i]-Ts)
    plot(l,T)
    show()
    pause(0.5)
    t=t+dt
print t


