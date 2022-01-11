# -*- coding: utf-8 -*-


#-------------Tracé des fonctions de la question 1 2 3 et 5--------------#


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Rg=12
hg=1
L=np.arange(0.1,10**8,200000)
Rastro=0.1
fbio=1

c=(3.0*10**8)
N=L*Rastro*fbio



    
def Distance(Rg,hg,N):
    D=np.zeros(len(N))
    for i in range (len(N)):
        if N[i]>1000:
            D[i]=2*((3*hg*Rg**2)/(4*N[i]))**(1/3)
        else: 
                D[i]=2*Rg/np.sqrt(N[i])
    return D


def Fct_proba(L,N):
    Rast=1
    v=0.001*c
    F=np.zeros(len(N))
    for j in range (len(N)):
        if v*L[j]<hg:
            F[j]=(1/3*hg*Rg**2)*Rast*fbio*v*L[j]**4
        else:
              F[j]=(1/3*Rg**2)*Rast*fbio*v*L[j]**3
    return F


def Fct_proba2(L,N):
    Rast=0.1
    fbio=N/(L*Rast)
    v=0.001*c
    ne=Rast*fbio*L*(v*L)**2
    if v*L<hg:
        num=Rast*fbio*L*(v*L)**3
        den=hg*Rg**2
        return (1/3)*(num/den)
    return (1/3)*(ne/Rg**2)


def Fct_proba3(L,N):
    v=0.001*c
    if v*L<hg:
        return (N*(v*L)**3)/(3*hg*Rg**2)
    return (N*(v*L)**2)/(3*Rg**2)
 
def Fct_proba4(L,N):
    v=0.001*c
    if v*L<hg:
        return (N*(v*L)**3)/(3*hg*Rg**2)
    return (N*(v*L)**2)/(3*Rg**2)  
    
[X,Y]=np.meshgrid(L,N)
fig, ax = plt.subplots(1, 1) 
Fct_probav = np.vectorize(Fct_proba3)
Z = Fct_probav(X,Y)

levels=[1,0.1,0.001,0.0001]
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Proba de contact v=0.001c ')    
fig.colorbar(CS) # Add a colorbar to a plot
ax.set_xlabel('L ann') 
ax.set_ylabel('N') 


plt.plot(L,N) 
plt.show() 





#Tracage de D et N en fct de L sur une même figure 
fig=plt.figure()
ax=fig.add_subplot(111, label="1")
ax3=fig.add_subplot(111, label="3", frame_on=False)

ax.plot(L,N, color="C0")
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("L", color="C0")
ax.set_ylabel("N", color="C0")
ax.tick_params(axis='x', colors="C0")
ax.tick_params(axis='y', colors="C0")
plt.title("fbiotec=1")

ax.plot(L,L*Rastro*0.1, color="g")
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("L", color="g")
ax.set_ylabel("N", color="g")
ax.tick_params(axis='x', colors="g")
ax.tick_params(axis='y', colors="g")
plt.title("fbiotec=0.1")

ax.plot(L,L*Rastro*0.0001, color="m",label=Distance)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("L", color="m")
ax.set_ylabel("N", color="m")
ax.tick_params(axis='x', colors="m")
ax.tick_params(axis='y', colors="m")
plt.title("fbiotec=0.0001")

ax.plot(L,L*Rastro*10**-6, color="b")
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("L (ann)", color="b")
ax.set_ylabel("N", color="b")
ax.tick_params(axis='x', colors="b")
ax.tick_params(axis='y', colors="b")
ax.set_xlim(1,10**8)
ax.set_ylim(0.1)
plt.title("fbiotec=10**-6")

ax3.plot(L,Distance(Rg,hg,N),label=Distance, color="r")

ax3.set_ylabel("Distance (ann.l)", color="r")
ax3.tick_params(axis='x', colors="r")
ax3.tick_params(axis='y', colors="r")
ax3.yaxis.tick_right()
ax3.yaxis.set_label_position('right') 
ax3.set_xscale('log')
ax3.set_yscale('log')
plt.xlim(1,10**8)


fig.suptitle('Nombres de civilisations et distance en fonction de L',fontsize=16)

plt.show()
