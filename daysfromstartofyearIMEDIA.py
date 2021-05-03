#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:27:58 2021

@author: utilisateur
"""

import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np 

transchoice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  

#plt.figure(figsize = (11, 7)) #largeur puis hauteur

for p in transchoice:
        xL=[]

        
        IMEDIA = xr.open_dataset("profil" + str(p) +".nc", decode_times=True)
        time=IMEDIA['TIME']
        temp=IMEDIA['TEMP']
        d=IMEDIA['DEPTH']
        psal=IMEDIA['PSAL']
        pression=IMEDIA['P']
        absolute=IMEDIA['SA']
        num=IMEDIA['NUM']
        massvol=IMEDIA['RHO']

        day, year = time[:], 2012
        xL.append(pd.to_datetime(day-1, unit='D', origin=str(year)))
        xL=np.array(xL[0])                                                          

        plt.gca().invert_yaxis()           

        plt.figure(figsize = (11, 7))
        plt.xlim([xL[0],xL[-1]])
        plt.gca().invert_yaxis()           
        plt.ylabel("depth (m)", size = 14)
        plt.xlabel("time (day - hr)", size = 13, position =(1,1))                
        plt.scatter(xL, d, 40, massvol, cmap='bone')

        plt.colorbar()#boundaries=np.linspace(12, 14))
        
        plt.clim(1028.8,1031)
        #plt.xlim('2012-03-15T16:04:46.161427200','2012-03-15T21:57:06.000019200')
        
        plt.ylim(0,420)
        plt.gca().invert_yaxis() 
        plt.savefig('rho' + str(p) + '.png')
        
