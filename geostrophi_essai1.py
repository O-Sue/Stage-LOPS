#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:21:13 2021

@author: utilisateur
"""

import xarray as xr
import numpy as np
from gsw.geostrophy import geo_strf_dyn_height as geodyn 
from gsw.geostrophy import geostrophic_velocity as v_geo 
import pandas as pd



transchoice = [1]#, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  


for p in transchoice:

        IMEDIA = xr.open_dataset("../data/ncforgeos/averaged/profil" +str(p) + "_geos.nc", decode_times=True)      # ../chemin d'accès sous machine eos/ + ".." pour retour d'un répertoirpar rapport à où il est.
        lat=IMEDIA['LAT']
        lon=IMEDIA['LON']
        rad=IMEDIA['TIME']  
        lat= np.array(lat.data)
        lon= np.array(lon.data)
        lon=lon.reshape(1,len(rad))    
        lat=lat.reshape(1,len(rad))                                                          # -> len(time) donne num de radiale
                                                                                            # -> len(time) donne num de radiale
        S=IMEDIA['SA']                                                                  #salinité absolue en g.kg-1
        num=IMEDIA['N_LEVEL']                                                           #liste de 0 à 49 / nombre de profondeurs
        P=IMEDIA['P']                                                                   #pression en db
        T=IMEDIA['CT']                                                                  #température

        
        for j in range(len(rad)) :
        
            hdyn=geodyn(S[j, :], T[j, :], P[:], p_ref)   #p_ref =P[np.where(...) 
            print(hdyn)
            v = v_geo(hdyn[:],lon[j],lat[j]) 

        
        
            #print(hdyn)
            print(v)
            
