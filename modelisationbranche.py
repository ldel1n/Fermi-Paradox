# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:12:39 2021

@author: mouli
"""
#------------modelisation d'apparition de N civilisations en cartesien en fct du temps---------#
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

from scipy.stats import bernoulli
from scipy import signal

l=3/40000
ra=1.5
V=4*np.pi*ra**3
c=3*10**8
a=40000 
N=1000
H=3260
t=[0,10**3,10**6,10**9,10**11]


#coord étoiles
u=[0,0,0,0,0]
phi=[0,0,0,0,0]
h=[0,0,0,0,0]
r=[0,0,0,0,0]
pciv=[0,0,0,0,0]
coord=[0,0,0,0,0]
coordbis=[0,0,0,0,0]
xciv=[0,0,0,0,0]
yciv=[0,0,0,0,0]
hciv=[0,0,0,0,0]
n=[0,0,0,0,0]
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

for i in range(len(t)):
    
    n[i]=rd.binomial(1,0.5,N) #tire sur quelle branche va être le point
    u[i]=rd.uniform(0,1,N)
    phi[i]=rd.uniform(0,2*np.pi,N)
    h[i]=rd.normal(0,H/3,N)
    r[i]=-(1/l)*np.log(1-u[i])

    
    #dans le repères de la branche
    d[i]=rd.normal(0,40000/12000,N) #distance point branche
    x[i]=r[i]-(r[i]/a)*(d[i]/np.sqrt((r[i]**2/a**2)+1)) #coord étoile dans ref branche
    y[i]=d[i]*a/np.sqrt(r[i]**2+a**2)
    
    #changement de base avec matrice passage u=cos x ; sin x et v=-sinx ; cos x
    

    xp[i]=x[i]*np.cos(phi[i]+np.pi*n[i])-y[i]*np.sin(phi[i]+np.pi*n[i])
    yp[i]=x[i]*np.sin(phi[i]+np.pi*n[i])+y[i]*np.cos(phi[i]+np.pi*n[i])
    
    
    """xb1[i]=x[i]*np.cos(phi[i])-y[i]*np.sin(phi[i])
    yb1[i]=x[i]*np.sin(phi[i])+y[i]*np.cos(phi[i])        
        
    coord[i]=[xp[i],yp[i],h[i]]
    coord1[i]=[xb1[i],yb1[i],h[i]]
    
    coord1bis[i]=(n[i])*coord1[i] 
    coordbis[i]=n[i]*coord[i] 
    
    C=np.reshape(coordbis[i],(3,N))


    xp[i]=C[:1][np.where(C[:1]!=0)]
    yp[i]=C[1:2][np.where(C[1:2]!=0)]
    h[i]=C[2:3][np.where(C[2:3]!=0)]
        
    xb1[i]=C[:1][np.where(C[:1]==0)]
    yb1[i]=C[1:2][np.where(C[1:2]==0)]
    h[i]=C[2:3][np.where(C[2:3]==0)]     """
    

        

#Planètes 

    fig=plt.figure()
    ax=plt.axes(projection="3d")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('h')
    
    
    dr=4*np.pi*(ra**2)*(0.01*c*10**-16)

  #  s[i]=sb
 #   w=np.ones(len(r[i]))*dr+V
  #  v=np.ones(len(r[i]))*V
   # s=np.append(w,v)
    #ax.scatter3D(np.append(xp[i],xp[i+1]),np.append(yp[i],yp[i+1]),np.append(h[i],h[i+1]),s=10,c="g")
    
    ax.scatter3D(xp[i],yp[i],h[i],) #np.ones(len(xp[i])*(V+dr))
    ax.scatter3D(xp[i-1],yp[i-1],h[i-1],s=V+dr,c='g')
   # plt.show()


  #  fig = plt.figure()

  #  ax = fig.add_subplot(111, projection='polar')
   # ax.scatter(np.append(xp[i],xp[i+1]),np.append(yp[i],yp[i+1]),np.append(h[i],h[i+1]),s=10)

  #  ax.scatter(xp[i],yp[i],h[i],) #np.ones(len(xp[i])*(V+dr))
   # ax.scatter(xp[i-1],yp[i-1],h[i-1],s=10,c='g')
    plt.show() 
    
    

    
#si étoiles a une planète habitable
    pciv[i]=rd.binomial(1,0.1,N)

    coord[i]=[xp[i],yp[i],h[i]]
    coordbis[i]=pciv[i]*coord[i] 
    C=np.reshape(coordbis[i],(3,N))

    xciv[i]=C[:1][np.where(C[:1]!=0)]
    yciv[i]=C[1:2][np.where(C[1:2]!=0)]
    hciv[i]=C[2:3][np.where(C[2:3]!=0)]
    
    
    #Planètes 

    fig=plt.figure()
    ax=plt.axes(projection="3d")
    ax.set_xlabel('r')
    ax.set_ylabel('phi')
    ax.set_zlabel('h')
      
    ax.scatter3D(xciv[i],yciv[i],hciv[i],) #np.ones(len(xp[i])*(V+dr))
    ax.scatter3D(xciv[i-1],yciv[i-1],hciv[i-1],s=V+dr,c='g')
        
    

    plt.show()
    

    
    