# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 17:48:58 2021

@author: mouli
"""
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import matplotlib.patches as mpatches

from scipy.stats import bernoulli
from scipy import signal

l=3/40000
ra=1
V=4*np.pi*ra**3
c=3*10**8
a=40000
Ne=100
N=8*10**3
H=3260
t=[0,10**3,10**6,10**9,10**11]
L=10**6
v=0.001*c
dr=4*np.pi*v*10**10

#coord étoiles
u=[0,0,0,0,0]
phi=[0,0,0,0,0]
h=[0,0,0,0,0]
pciv=[0,0,0,0,0]
coord=[0,0,0,0,0]
coordbis=[0,0,0,0,0]
xciv=[0,0,0,0,0]
yciv=[0,0,0,0,0]
hciv=[0,0,0,0,0]
d=[0,0,0,0,0]
x=[0,0,0,0,0]
xp=[0,0,0,0,0]
y=[0,0,0,0,0]
yp=[0,0,0,0,0]
xb2=[0,0,0,0,0]
yb2=[0,0,0,0,0]
hb2=[0,0,0,0,0]
xb1=[0,0,0,0,0]
yb1=[0,0,0,0,0]
coord1=[0,0,0,0,0]
coord1bis=[0,0,0,0,0]

a=40000/(2*np.pi)

ni=rd.binomial(1,0.1,Ne) #tire sur quelle branche va être le point
ui=rd.uniform(0,1,Ne)
hi=rd.normal(0,H/3,Ne)
ri=-(1/l)*np.log(1-ui)

n=[0,0,0,0,0]
r=[0,0,0,0,0]
rciv=[0,0,0,0,0]
rcivi=ri*ni

for i in range(0,len(t)):
        
    dr=4*np.pi*(ra**2)*(0.01*c)*10**-7
    
    n[i]=rd.binomial(1,0.5,N) #tire sur quelle branche va être le point
    u[i]=rd.uniform(0,1,N)
    phi[i]=rd.uniform(0,2*np.pi,N)
    h[i]=rd.normal(0,H/3,N)
    r[i]=-(1/l)*np.log(1-u[i])


    
    #dans le repères de la branche
    d[i]=rd.normal(0,40000/12000,N) #distance point branche
    x[i]=r[i]-(r[i]/a)*(d[i]/np.sqrt((r[i]**2/a**2)+1)) #coord étoile dans ref branche
    y[i]=d[i]*a/np.sqrt(r[i]**2+a**2)
    

    
    
    if (i)==0:
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        
        ax.scatter((ri/a),ri,s=V,c='purple')
        ax.scatter(((ri/a)+np.pi),ri,s=V, c='blue')
        plt.show() 
    
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
            
        ax.scatter(rcivi/a,rcivi,s=V,c='green')
        ax.scatter(((rcivi/a)+np.pi)*ni,rcivi,s=V, c='blue')
        
        plt.show() 
    
    else:
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        
        r[0]=ri
        ax.scatter(r[i]/a,r[i],s=V,c='purple') #np.ones(len(xp[i])*(V+dr))
        ax.scatter(r[i-1]/a,r[i-1],s=V+dr,c='cyan')
        ax.scatter((r[i]/a)+np.pi,r[i],s=V, c='blue') #np.ones(len(xp[i])*(V+dr))
        ax.scatter((r[i-1]/a)+np.pi,r[i-1],s=V+dr, c='pink')
    
        ep= mpatches.Patch(color='purple', label='étoiles bras 1')
        ecb=mpatches.Patch(color='cyan', label='étoiles âgées bras 1')
        eb=mpatches.Patch(color='blue', label='étoiles bras 2')
        epb=mpatches.Patch(color='pink', label='étoiles âgées bras 2')
    
        plt.legend(handles=[ep,ecb,eb,epb] ,bbox_to_anchor=(1.05, 1))
        
        plt.show() 
    
    
        rciv[i]=r[i]*pciv[i]
#si étoiles a une planète habitable
        pciv[i]=rd.binomial(1,0.1,N)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')

        rciv[0]=rcivi
        c1=ax.scatter((rciv[i]/a),rciv[i],s=V,c='purple') #np.ones(len(xp[i])*(V+dr))
        c1i=ax.scatter((rciv[i-1]/a),rciv[i-1],s=V+dr,c='cyan')
        c2=ax.scatter((rciv[i]/a)+np.pi,rciv[i],s=V,c='blue') #np.ones(len(xp[i])*(V+dr))
        c2i=ax.scatter((rciv[i-1]/a)+np.pi,rciv[i-1],s=V+dr,c='pink')
    
        p= mpatches.Patch(color='purple', label='Civ bras 1')
        cb=mpatches.Patch(color='cyan', label='Civ âgées bras 1')
        b=mpatches.Patch(color='blue', label='Civ bras 2')
        pb=mpatches.Patch(color='pink', label='Civ âgées bras 2')
    
        plt.legend(handles=[p,cb,b,pb] ,bbox_to_anchor=(1.05, 1))
        
    
    
    
        plt.show() 
    