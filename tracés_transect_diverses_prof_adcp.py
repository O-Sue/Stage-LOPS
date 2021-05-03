#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:19:40 2021

@author: utilisateur
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


transchoice = [5]


for p in transchoice:
    #IMEDIA = xr.open_dataset("courants_IMEDIA_TIE120" + str(p) +".nc", decode_times=True)
     
    #IMEDIA = xr.open_dataset("courants_IMEDIA_TIE120" + str(p) +"skaphi_14032012_reduc.nc", decode_times=True)
    
    IMEDIA = xr.open_dataset("courants_IMEDIA_TIE120" + str(p) + "sk_15032012_new_complete.nc", decode_times=True)
    lat=IMEDIA['LAT'] 
    lon=IMEDIA['LON'] 
    lat= np.array(lat.data)
    lon= np.array(lon.data)
    u=IMEDIA['U'][:,10]
    v=IMEDIA['V'][:,10]
    d=IMEDIA['DEPTH'][:,10]
    u=np.array(u.data)    # .data pour obtenir les données épurées du superflu/ np.array pour le forcer en type 
    v=np.array(v.data)


    u=u[::4]
    v=v[::4]
    lat=lat[::4]
    lon=lon[::4]  

    plt.figure(figsize=(25,25))
    
        
    mymap=Basemap(projection='merc',llcrnrlat=43.2,urcrnrlat=44.3,llcrnrlon=8.2,urcrnrlon=10.3,resolution='h')
        
    X, Y = mymap(lon, lat)    
    mymap.drawcoastlines()
    myparallels=np.arange(-90,90+1,1)    
    mymeridians = np.arange(-180,180+1,1) 
    mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=35)  
    mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=35)
    mymap.fillcontinents(color='0.83',lake_color='0.83',zorder=100)
    

    #mymap.plot(X,Y , '+')
    
    Resolution=np.hypot(u, v)
    mymap.quiver(X,Y,u,v, Resolution, width=0.0050, scale=3) 
    plt.rcParams['xtick.labelsize'] = 30
    plt.rcParams['ytick.labelsize'] = 30                       
    plt.colorbar(aspect=30, orientation = 'horizontal') 
    plt.clim(0,1.05)
    plt.figtext(0.5, 0.25, 'vitesse en m/s', size = 30)
    plt.ylabel("Lat", size = 30, position=(1,0.95))
    plt.xlabel("Lon", size = 30, position=(1,1))   
    plt.title("Courant horizontaux le long de la trajectoire de la campagne IMEDIA à la profondeur 50.5 m", position = (0.5, 1.1 ), size = 35)
    plt.savefig("50,5m TIE120" + str(p)+".png")

