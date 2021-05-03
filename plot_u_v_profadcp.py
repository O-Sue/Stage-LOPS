#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:20:09 2021

@author: utilisateur
"""



import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, atan2, radians
from matplotlib.pyplot import savefig
import xarray as xr



IMEDIA = xr.open_dataset("courants_IMEDIA_TIE1205sk_15032012_radialMVP10" +".nc", decode_times=True)

lat=IMEDIA['LAT'] 
lon=IMEDIA['LON'] 
lat= np.array(lat.data)
lon= np.array(lon.data)
u=IMEDIA['U']
v=IMEDIA['V']
d=IMEDIA['DEPTH']
u=np.array(u.data)    
v=np.array(v.data)

xL=[0]
n=0
R = 6373.0
d=d[1]                 

for i in range (len(lat)-1):
    
    lat1 = radians(lat[n])
    lon1 = radians(lon[n])
    lat2 = radians(lat[n+1])
    lon2 = radians(lon[n+1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
                
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    
    n=n+1
    
    xL.append(distance)
                
    s=sum(xL)
            
                
for i  in range (len(xL)-1):       
            
    xL[i+1]=xL[i]+xL[i+1]

s2,depth2=np.meshgrid(xL, d)


plt.subplot(2, 1, 1)
u2=np.transpose(u)                 
a=plt.pcolormesh(s2,depth2, u2) 
plt.gca().invert_yaxis() 
plt.gca().xaxis.set_visible(False)  
plt.colorbar(aspect=10) 
plt.ylabel("depth (m)", size = 14)
plt.clim(-0.4,0.8) 
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 12

plt.subplot(2, 1, 2)
u2=np.transpose(v)                 
a=plt.pcolormesh(s2,depth2, u2) 
plt.gca().invert_yaxis() 
plt.gcf().set_size_inches(15, 10)   ###taille figure 
plt.clim(-0.4,0.8) 
plt.colorbar(aspect=10) 
plt.ylabel("depth (m)", size = 14)
plt.xlabel("distance (Km)", size = 14,position =(0.9,1))
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 12

  
plt.savefig("radiale_u_v_MVP10"+".png")

            
            
