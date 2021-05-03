#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:48:29 2021

@author: utilisateur
"""
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

transchoice = [9,11]

plt.figure(figsize=(23,23))
    

        
for p in transchoice:
    
    IMEDIA = xr.open_dataset("profil" + str(p) + "_vgeos.nc", decode_times=True)
    IMEDIA2 = xr.open_dataset("courants_IMEDIA_TIE1205sk_15032012_radialMVP" + str(p) + ".nc", decode_times=True)
    IMEDIA3 = xr.open_dataset("courants_IMEDIA_TIE1205sk_15032012_radialMVP10.nc ", decode_times=True)   # espace des fois oui des fois non
    IMEDIA4 = xr.open_dataset("profil10_vgeos.nc", decode_times=True)

    lat=IMEDIA['LAT'] 
    lon=IMEDIA['LON'] 
    lat= np.array(lat.data)
    lon= np.array(lon.data)
    vgeo=IMEDIA['VGEO'][:, 5]                        
    vgeo= np.array(vgeo.data)
    P=IMEDIA['P'] 
    
    latx=IMEDIA4['LAT'] 
    lonx=IMEDIA4['LON'] 
    latx= np.array(latx.data)
    lonx= np.array(lonx.data)
    vgeox=IMEDIA4['VGEO'][:, 5]                         
    vgeox = np.array(vgeox.data)
    Px=IMEDIA['P'] 
    
    lat2=IMEDIA2['LAT'] [::10]
    lon2=IMEDIA2['LON'] [::10]
    lat2= np.array(lat2.data)
    lon2= np.array(lon2.data)
    u=IMEDIA2['U'][:,5]
    v=IMEDIA2['V'][:,5]
    d=IMEDIA2['DEPTH']
    u=np.array(u.data)    
    v=np.array(v.data)
    u=u[::10]
    v=v[::10]
    
    lat3=IMEDIA3['LAT'] [::10]
    lon3=IMEDIA3['LON'] [::10]
    lat3= np.array(lat3.data)
    lon3= np.array(lon3.data)
    w=IMEDIA3['U'][:,5]
    z=IMEDIA3['V'][:,5]
    d3=IMEDIA3['DEPTH']
    w=np.array(w.data)    
    z=np.array(z.data)
    w=w[::10]
    z=z[::10]
    
    
    
    alpha =  np.arctan2(lat2[-1]-lat2[0],lon2[-1]-lon2[0])  
    u_normal = -u[:]*np.sin(alpha)+v[:]*np.cos(alpha)
    
    alpha3 =  np.arctan2(lat3[-1]-lat3[0],lon3[-1]-lon3[0])  
    u_normal3 = -w[:]*np.sin(alpha3)+z[:]*np.cos(alpha3)
    
    mymap=Basemap(projection='merc',llcrnrlat=43.35,urcrnrlat=43.9,llcrnrlon=8.8,urcrnrlon=9.7,resolution='h')
      
    mymap.drawcoastlines()
    myparallels=np.arange(-90,90+1,0.8)    
    mymeridians = np.arange(-180,180+1,0.8) 
    mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=26)  
    mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=26)
    mymap.scatter(lon, lat, 80, vgeo, cmap='seismic', latlon=True, facecolors='none',alpha =0.5)
    mymap.scatter(lonx, latx, 80, vgeox, cmap='seismic', latlon=True, facecolors='none',alpha =0.5)
   
    X, Y = mymap(lon2, lat2)  
    X3, Y3 =mymap(lon3, lat3)  
    myparallels=np.arange(-90,90+1,1)    
    mymeridians = np.arange(-180,180+1,1) 
    mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=35)  
    mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=35)
    mymap.scatter(lon, lat, 60, vgeo, cmap='seismic', latlon=True)

    plt.clim(-0.6,0.6)
    plt.rcParams['xtick.labelsize'] = 35
    plt.rcParams['ytick.labelsize'] = 35
    Resolution=u_normal    # Sur quoi porte la colorbar (norme ou autre)
    mymap.quiver(X,Y,0 ,u_normal , Resolution, width=0.0050, scale=3, cmap='seismic') 
    mymap.quiver(X3,Y3,0 ,u_normal3 , u_normal3, width=0.0050, scale=3, cmap='seismic') 

    plt.clim(-0.6,0.6)
    plt.ylabel("Lat", size = 30, position=(1,0.95))
    plt.xlabel("Lon", size = 30, position=(1,1))
plt.colorbar(aspect =26, orientation ="horizontal")
     
plt.savefig("crosstrack"+".png")
    
