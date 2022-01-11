
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd
import matplotlib.patches as mpatches


#--------Tirage d'étoiles modèle bras spiraux en coord polaires---------#

l=3/40000
ra=1
V=4*np.pi*ra**3
c=3*10**-8
N=100
H=3260
t=[0,10**3,10**6,10**9,10**11]
L=10**6
v=0.004*c
dr=4*np.pi*v*10**10

ni=rd.binomial(1,0.1,N) #tire sur quelle branche va être le point
ui=rd.uniform(0,1,N)
phii=rd.uniform(0,2*np.pi,N)
hi=rd.normal(0,H/3,N)
ri=-(1/l)*np.log(1-ui) #méthode fct inverse
n1=rd.binomial(1,0.5,N)
n2=rd.binomial(1,0.5,N)
a=40000/(2*np.pi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
        
ax.scatter((ri/a)*n1,ri*n1,s=V+dr,c='purple')
ax.scatter(((ri/a)+np.pi)*n2,ri*n2,s=V+dr, c='blue')
plt.show() 
    
rciv1=ri*n1*ni
rciv2=ri*n2*ni       
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
            
c1=ax.scatter(rciv1/a,rciv1,s=V+dr,c='purple')
c2=ax.scatter(((rciv2/a)+np.pi)*ni,rciv2,s=V+dr, c='blue')

       
    
c1= mpatches.Patch(color='purple', label='Civ bras 1')
c2=mpatches.Patch(color='blue', label='Civ bras 2')

plt.title("N=10 v/c =0.004 ", loc="left")
plt.legend(handles=[c1,c2] ,bbox_to_anchor=(1.2, 1.2))
        
plt.show() 