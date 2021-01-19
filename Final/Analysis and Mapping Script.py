# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:41:56 2019

@author: Cole
"""
# =============================================================================
# Import Modules
import geopandas
import matplotlib.pyplot as plt
# =============================================================================
def CorrMeasures(shpFilePath, nameOfArea, extentX1 = None, extentX2 = None, extentY1 =None, extentY2=None):
   #error catch: if its not a shapefile...
    gdf= geopandas.read_file(shpFilePath)   
    world = gdf.cx[extentX1 : extentX2, extentY1 : extentY2]
    
    plt.scatter(x = world['pct frgn'], y = world['LQ'])
    plt.ylabel('Location Coefficent')
    plt.xlabel('Percent Foreign Born')
    plt.show()
    print('correlation coefficent, percent foreign born =', world['pct frgn'].corr(world['LQ']))

    plt.scatter(x = world['pct black'], y = world['LQ'])
    plt.ylabel('Location Coefficent')
    plt.xlabel('Percent Black')
    plt.show()
    print('correlation coefficent, percent black =', world['pct black'].corr(world['LQ']))

    plt.scatter(x = world['per capita'], y = world['LQ'])
    plt.ylabel('Location Coefficent')
    plt.xlabel('per captita income')
    plt.show()
    print('correlation coefficent, per capita income =', world['per capita'].corr(world['LQ']))
    print('\n')
      
    fig, ax = plt.subplots(1, figsize = (10,10))
    world.plot(column = 'LQ', 
               alpha = 1, 
               linewidth=0.05, 
               edgecolor='black', 
               ax=ax, 
               legend=True,
               cmap= 'PuBu',
               scheme = 'user_defined',
               classification_kwds = {'bins':[1,5,10,25,50,100,200]}) 
    nameFile = "{}_map.jpg".format(nameOfArea)
    plt.savefig(nameFile, dpi=500)
    
CorrMeasures(r'C:\Users\Cole\Documents\GitHub\class-project-and04671\SHP Files\2010File.shp','MN2010',-1000, 450000, 650000, 1300000)
CorrMeasures(r'C:\Users\Cole\Documents\GitHub\class-project-and04671\SHP Files\2012File.shp','MN2012',-1000, 450000, 650000, 1300000)
CorrMeasures(r'C:\Users\Cole\Documents\GitHub\class-project-and04671\SHP Files\2015File.shp','MN2015',-1000, 450000, 650000, 1300000)

