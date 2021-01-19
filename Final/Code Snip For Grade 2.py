# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:24:26 2019

@author: Cole
"""

import geopandas
import matplotlib.pyplot as plt
# =============================================================================
#same global variables to denote folder structure relative to file
directory = r"C:\Users\Cole\Documents\GitHub\class-project-and04671\\"
shpFilePath = directory + 'SHP Files\\'

def CorrMeasures(shpFile, nameOfArea, extentX1 = None, extentX2 = None, extentY1 =None, extentY2=None):
   """
   Function takes in shapefile with possibility for limiting calculation extents, returns correlation
   field values and LQs, and saves a map file of the extent
   
   Inputs:
       shapefile with demography
       the name of the area calculated for
       optional: limiting extents
   Outputs:
       correlation R vals
       Map to file
   """
   #creates file path from shp File
   filePath = shpFilePath + shpFile
   #uses geopandas to creates a geo-dataframe of file
   gdf= geopandas.read_file(filePath)
   #creates snipped extent based on supplied values      
   world = gdf.cx[extentX1 : extentX2, extentY1 : extentY2]
     
   #calculates and prints the R value between each specified marker and LQ
   for each in ['pct frgn','pct black','per capita']:
        print('correlation coefficent', each, '=', world[each].corr(world['LQ']))
        print('\n')
   #setup for map: denotes desired figure and legend size
   fig, ax = plt.subplots(1, figsize = (10,10))
   #plots the extent with variety of design specs: color map, user defined class scheme
   world.plot(column = 'LQ', 
               alpha = 1, 
               linewidth=0.05, 
               edgecolor='black', 
               ax=ax, 
               legend=True,
               cmap= 'PuBu',
               scheme = 'user_defined',
               classification_kwds = {'bins':[1,5,10,25,50,100,200]}) 
   #names the file for export, based on given area
   nameFile = "{}_map.jpg".format(nameOfArea)
   #saves at specific resolution
   plt.savefig(nameFile, dpi=500)
#calls the function for each year in the list   
for each in ['2010','2012','2015']:
    CorrMeasures(each + 'File.shp','MN'+ each, -1000, 450000, 650000, 1300000)