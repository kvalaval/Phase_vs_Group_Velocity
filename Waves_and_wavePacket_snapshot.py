# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:25:30 2021

@author: vasan
"""

#The goal of this script is to show phase velocity and group velocity formulas:
import numpy as np
import matplotlib.pyplot as plt

#I will first plot time independent waave form and time independent wave packet. 
#Later on, I will add time dependence and animations of the wave forms
num=11 #number of k values to used to form wave packet
fig,ax=plt.subplots(num+1,1,sharex=True,figsize=(16,12))
x=np.linspace(-10,10,1001) #Generating discreete x-points with a pitch of 0.01
wavePack=np.zeros(x.shape)
waveL=1
k=2*np.pi/waveL
dk=0.33*k
kar=np.linspace(k-dk/2,k+dk/2,num)
for a in range(len(kar)):
    if kar[a]==k:
        ax[a].plot(x,np.cos(kar[a]*x),label='k = '+str(round(kar[a]/np.pi,3))+r'$\pi$',linewidth=1.5,color='#fc4f30')
    else:
        ax[a].plot(x,np.cos(kar[a]*x),label='k = '+str(round(kar[a]/np.pi,3))+r'$\pi$',linewidth=1.5)
    ax[a].legend(loc='upper right')
    wavePack+=np.cos(kar[a]*x)

ax[num].plot(x,wavePack,label=r'$\sum_{k=1.67\pi}^{2.33\pi}$', color='r',linewidth=3)
ax[num].legend(loc='upper right')
ax[num].set_xlabel('X',fontsize=18)
plt.show()


    
    
    