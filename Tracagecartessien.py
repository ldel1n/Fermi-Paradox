# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:32:41 2021

@author: mouli
"""
#---------------Simulation via le model plus sophistiqué--------#


import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

from scipy.stats import bernoulli
from scipy import signal

l=3/40000
ra=1
V=4*np.pi*ra**3
c=3*10**8
a=40000 
N=3000
H=3260
a=40000/(2*np.pi)

n1=rd.binomial(1,0.5,N) #tire sur quelle branche va être le point
n2=rd.binomial(1,0.5,N)


u=rd.uniform(0,1,N)
#phi=rd.uniform(0,2*np.pi,N)
h=rd.normal(0,H/3,N)
r=-(1/l)*np.log(1-u)
phi=r/a


    
#dans le repères de la branche
d=rd.normal(0,40000/50,N) #distance point branche
x=r-(r*d/np.sqrt(a**2+r**2))
y=(d*a)/np.sqrt(r**2+a**2)
    
#changement de base avec matrice passage u=cos x ; sin x et v=-sinx ; cos x
    
x1=(x*np.cos(phi+np.pi)-y*np.sin(phi+np.pi))*n1 #branche 1 
y1=(x*np.sin(phi+np.pi)+y*np.cos(phi+np.pi))*n1

x2=(x*np.cos(phi)-y*np.sin(phi))*n2 #branche 2 symétrique à 1 (enlève pi)
y2=(x*np.sin(phi)+y*np.cos(phi))*n2

h1=h*n1
h2=h*n2



new_x1=np.delete(x1, np.where((x1<=0)&(x1>=0)))
new_y1=np.delete(y1, np.where((y1<=0)&(y1>=0)))
new_x2=np.delete(x2, np.where((x2<=0)&(x2>=0)))
new_y2=np.delete(y2, np.where((y2<=0)&(y2>=0)))
new_h1=np.delete(h1, np.where((h1<=0)&(h1>=0)))
new_h2=np.delete(h2, np.where((h2<=0)&(h2>=0)))


#Planètes 

fig=plt.figure()
ax=plt.axes(projection="3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.scatter3D(new_x1,new_y1,new_h1,c="blue") 
ax.scatter3D(new_x2,new_y2,new_h2,c='purple')

plt.title("Apparition de civilisations dans un model plus sophistiqué")
plt.show() 

#si étoiles a une planète habitable
na=rd.binomial(1,0.1,N)
nb=rd.binomial(1,0.1,N)



xp1=x1*na
yp1=y1*na

xp2=x2*nb
yp2=y2*nb

hp1=h1*na
hp2=h2*nb

new_xp1=np.delete(xp1, np.where((xp1<=0)&(xp1>=0)))
new_yp1=np.delete(yp1, np.where((yp1<=0)&(yp1>=0)))
new_xp2=np.delete(xp2, np.where((xp2<=0)&(xp2>=0)))
new_yp2=np.delete(yp2, np.where((yp2<=0)&(yp2>=0)))
new_hp1=np.delete(hp1, np.where((hp1<=0)&(hp1>=0)))
new_hp2=np.delete(hp2, np.where((hp2<=0)&(hp2>=0)))


fig=plt.figure()
ax=plt.axes(projection="3d")

ax.scatter3D(new_xp1,new_yp1,new_hp1,s=0.1,c="blue") 
ax.scatter3D(new_xp2,new_yp2,new_hp2,s=0.1,c='purple')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
      
r1=(new_xp1**2+new_yp1**2)**(1/2)
r2=(new_xp2**2+new_yp2**2)**(1/2)
    
t1=np.arctan(new_yp1/new_xp1)
t2=np.arctan(new_yp2/new_xp2)

"""r1=(xp1**2+yp1**2)**(1/2)
r2=(xp2**2+yp2**2)**(1/2)
    
t1=np.arctan(yp1/xp1)
t2=np.arctan(yp2/xp2)"""

#vu du dessus
plt.title("Apparition de civilisations N=300 model plus sophistiqué")
plt.show()

fig = plt.figure()
ax=plt.axes()
        
ax.scatter(new_xp1,new_yp1,s=0.1,c="blue")
ax.scatter(new_xp2,new_yp2,s=0.1,c="purple")

ax.set_xlabel('x')
ax.set_ylabel('y')
plt.title("Vu du dessus N=300")
plt.show()

#vu de cote

plt.show()

fig = plt.figure()
ax=plt.axes()
ax.set_xlabel('x')
ax.set_ylabel('z') 
ax.scatter(new_xp1,new_hp1,s=0.1,c="blue")
ax.scatter(new_xp2,new_hp2,s=0.1,c="purple")
plt.title("Vu latéral N=300")

plt.show()