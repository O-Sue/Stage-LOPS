#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:40:44 2021

@author: utilisateur
"""
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap





transchoice = [8]#, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  


for p in transchoice:
        
        IMEDIA = xr.open_dataset("profil" + str(p) +".nc", decode_times=True)
        time=IMEDIA['TIME']
        temp=IMEDIA['TEMP']
        d=IMEDIA['DEPTH']
        psal=IMEDIA['PSAL']
        pression=IMEDIA['P']
        absolute=IMEDIA['SA']
        num=IMEDIA['NUM']
        massvol=IMEDIA['RHO']

        lat=IMEDIA['LAT']
        lon=IMEDIA['LON']
        lat= np.array(lat.data)
        lon= np.array(lon.data)

        
      

plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13
           
plt.subplot(2, 2, 1)
plt.axis('off')
mymap=Basemap(projection='merc',llcrnrlat=42,urcrnrlat=45,llcrnrlon=5.9,urcrnrlon=10,resolution='h')            
mymap.drawcoastlines()
myparallels=np.arange(-90,90+1,2)    #  le dernier 1 affiche tout les 1 lon/lat en légende/quadrillage
mymeridians = np.arange(-180,180+1,3) 
mymap.drawparallels(myparallels,labels=[1,0,0,0],fontsize=13)  
mymap.drawmeridians(mymeridians,labels=[0,0,0,1],fontsize=13)
mymap.fillcontinents(color='0.83',lake_color='0.83',zorder=100)      
mymap.scatter(lon, lat, latlon=True, s=10)
plt.gcf().subplots_adjust(  wspace = 0.28)




plt.subplot(2, 2, 2)
plt.gca().invert_yaxis()           
plt.gcf().set_size_inches(15, 10)        
plt.ylabel("depth (m)", size = 14)
plt.scatter(lat, d , 40, temp, cmap='hot')
plt.colorbar()
plt.clim(12.7,14)
plt.xlim([lat[0],lat[-1]])


       
plt.subplot(2,2, 3)

plt.gca().invert_yaxis()           
plt.gcf().set_size_inches(15, 10)        
plt.ylabel("depth (m)", size = 14)
plt.scatter(lat, d , 40, massvol, cmap='inferno_r')
plt.colorbar()
plt.xlim([lat[0],lat[-1]])
plt.clim(1029,1031)



plt.subplot(2, 2, 4)
            
plt.gca().invert_yaxis()           
plt.gcf().set_size_inches(15, 10)
        #plt.figure(figsize = (11, 7))
        #plt.xlim([xL[0],xL[-1]])
        #plt.gca().invert_yaxis()           
plt.ylabel("depth (m)", size = 14)
plt.xlabel("Lat", size = 16, position =(1,1))                
plt.scatter(lat, d , 40, psal, cmap='gnuplot2')
plt.colorbar()
#plt.xlim([lat[0],lat[-1]])

plt.xlim([lat[0],lat[-1]])
plt.clim(38.65,38.05)
        #plt.clim(38.85,38.25)
        #________________________________________________________________________
        #plt.ylim(0,420)
        #plt.gca().invert_yaxis() -> pour le transect 12 uniquement
        #-------------
        
plt.savefig('sublot' + str(p) + '.png')

        
        
        
        
                #plt.xlim([xL[0],xL[-1]])
