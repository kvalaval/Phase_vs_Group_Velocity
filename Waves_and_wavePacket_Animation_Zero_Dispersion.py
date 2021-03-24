# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:25:30 2021

@author: vasan
"""

#The goal of this script is to show phase velocity and group velocity formulas:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


knum=11 #number of k values to used to form wave packet
waveL=1 #Wavelength of a wave that will be part of a wave packet alongside its k-neighbors. We will call this the median wave.
k=2*np.pi/waveL #k-vector of the median wave
dk=0.33*k #uncertainty in k. Wave packet will be generated by summing over k values in range k-0.5dk to k+0.5dk
karray=np.linspace(k-dk/2,k+dk/2,knum) #array of k values for waves that will be summed to form the wave packet
freq=1 #frequency of the median wave in cycles/sec

ck=2*np.pi*freq/karray #phase velocity of all the waves that will be summed to form the wave packet
#Here,choosing all waves to have same frequency, zero dispersion case

x=np.linspace(-10,10,1001) #Generating discreete x-points with a pitch of 0.01
times=np.linspace(0,4/freq,401) #plotting for a period of 4 cycles of the median wave
yData=np.zeros((len(times),knum+1,1001)) # Clearly, the three axes of this data array are (time, k, Y)
#each row in y will have y-data for one wavelength (or k). 
#The last row will have the y-data for the wavepacket

for ti in range(len(times)):
    for ki in range(len(karray)):
        t,kw,cw=times[ti],karray[ki],ck[ki]
        yData[ti,ki,:]=np.cos(kw*x-cw*kw*t)
yData[:,-1,:]=yData.sum(axis=1)


fig,ax=plt.subplots(knum+1,1,sharex=True,figsize=(16,12))
lines=[]
for a in range(len(karray)):
    if karray[a]==k:
        line,= ax[a].plot(x,yData[0,a,:],label='k = '+str(round(karray[a]/np.pi,3))+r'$\pi$',linewidth=1.5,color='#fc4f30')
    else:
        line,=ax[a].plot(x,yData[0,a,:],label='k = '+str(round(karray[a]/np.pi,3))+r'$\pi$',linewidth=1.5,color= '#30a2da')
    
    lines.append(line)
    ax[a].legend(loc='upper right')

wpln,=ax[knum].plot(x,yData[0,-1,:],label=r'$\sum_{k=1.67\pi}^{2.33\pi}$', color='r',linewidth=3)
lines.append(wpln)

ax[knum].legend(loc='upper right')
ax[knum].set_xlabel('X',fontsize=18)

#creating a figure object and knum+1 axes objects. The last one will be the wave packet.


def update(ti):
    print(ti)
    for a in range(len(karray)):
        lines[a].set_data(x,yData[ti,a,:])
    lines[knum].set_data(x,yData[ti,-1,:])
    
ani=FuncAnimation(fig,update,frames=range(len(times)),interval=0,blit=False,repeat=False)
ani.save('Zero_dispersion.mp4', fps=1/times[1], dpi=120) #Frame per second controls speed, dpi controls the quality 

plt.show()


    
    
    