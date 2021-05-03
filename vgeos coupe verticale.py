#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:44:12 2021

@author: utilisateur
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, sqrt, atan2, radians
from scipy.ndimage.filters import gaussian_filter
plt.figure(figsize=(30,23))

sigma = 0.7 
IMEDIA = xr.open_dataset("profil12_vgeos.nc", decode_times=True)
IMEDIA2 = xr.open_dataset('profil12_geos.nc', decode_times=True)
density=IMEDIA2['PRHO'] 
density = (density[0:]+density[:-1])/2   #Réduis la taille de 1 en moyennant
latx=IMEDIA['LAT'] 
lonx=IMEDIA['LON'] 
latx= np.array(latx.data)
lonx= np.array(lonx.data)
density=np.array(density.data)
lat=IMEDIA['LAT'] 
lon=IMEDIA['LON'] 
lat= np.array(lat.data)
lon= np.array(lon.data)
vgeo=IMEDIA['VGEO']                         #vgeo.shape renvoi (60, 50) donc choix d'une profondeur particulière
vgeo= np.array(vgeo.data)
P=IMEDIA['P'] 
xL=[0]
yL=[0]
n=0
m=0
R = 6373.0
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
        
            
for i  in range (len(xL)-1):       #pas besoin de recréer une liste
        
        xL[i+1]=xL[i]+xL[i+1]
        

        
s2,depth2=np.meshgrid(xL, P)
print (density.shape)
print(type(density))
dens=np.transpose(density) 
plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30
u2=np.transpose(vgeo)                 
a=plt.pcolormesh(s2,depth2, u2, cmap='seismic') 
plt.gca().invert_yaxis() 

dens=gaussian_filter(dens, sigma)

cont=plt.contour(s2, depth2, dens, 5, colors="black")
plt.clabel(cont, inline=True, fontsize= 30)
plt.clim(-0.6,0.6)  
#plt.colorbar(aspect=10) 
plt.ylabel("depth (m)", size = 35, position=(1,0.95))
plt.savefig("anomaliesdensitépotentielleisopycne"+".png")
