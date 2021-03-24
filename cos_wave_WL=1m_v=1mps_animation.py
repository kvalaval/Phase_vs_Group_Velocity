# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:06:33 2021

@author: vasan
"""

import numpy as np
import math, time
pi=math.pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

x = np.linspace(-5,5,1001) #in m
waveL=1 # in m 
v_ph=1 #Phase velocity in m/s
freq=v_ph/waveL #in cycles per sec
y=np.cos(2*pi*x/waveL)

#creating an instances of figure, axes, axis labels, axis text
fig,ax=plt.subplots(figsize=(16,9))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(-5.2,5.2)
ax.set_ylim(-1.1,1.1)
axtext=ax.text(4.75,0.95,'0 s')
line1,line2,= ax.plot([],[],'#fc4f30',[waveL/8],[pi/4],'ko')
#Tip: plot is expected to return multiple line objects setting a comma at the end i.e line1, = assures that line1 is the handle for the first line object crated and not the list of line objects

t0=time.time()
def update_traveling_wave(t):
    y=np.cos(2*pi*x/waveL-2*pi*freq*t)
    line1.set_data(x, y)
    line2.set_data(waveL/8+v_ph*t,np.cos(pi/4))
    axtext.set_text('t = '+str(round(t,3))+'s')         
   

timestamps=np.linspace(0,4/freq,401) #plotting 4 cycles
ani=FuncAnimation(fig,update_traveling_wave,frames=timestamps, interval=timestamps[1]*1000,blit=False,repeat=False)
#This function repeated calls update_traveling_wave function and updates the line object. 
#**IMPORTANT** : when the animation is displayed, frames are updated every (interval + function calculation time).
#If you want to see your animation match real clock time, you can save it as an mp4 while setting appropriate fps rate

plt.show()
    
ani.save('cos_wave_WL=1m_v=1mps.mp4', fps=1/timestamps[1], dpi=120) #Frame per second controls speed, dpi controls the quality 

fig2,ax2=plt.subplots(figsize=(16,9))
ax2.plot(x,y,'#fc4f30',[waveL/8],[pi/4],'ko')
fig2.show()
fig2.savefig('cos_wave_WL=1m_t=0.png',dpi=100)
