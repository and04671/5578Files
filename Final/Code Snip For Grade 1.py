# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:20:50 2019

@author: Cole
"""
import pandas as pd
import geopandas
import os

#some of only globals in script, used to show folder associations to GIT base   
directory = r"C:\Users\Cole\Documents\GitHub\class-project-and04671\\"
#raw downloaded files
rawfilepath = directory + 'Raw\\'
#the joined demogrphy files PRE shapefile
joinedfilepath = directory + 'Joined\\'
#the output shapefiles
shpfilepath = directory + 'SHP Files\\'

def JoinStatstoSHP(JoinedFile, inshpfile, outshpfile):
    """
    This function takes file of attributes and joins them to a specified shapefile, 
    outputtng the result as a new shapefile in a specified location
    
    Inputs: 
        the joined demography file
        the shape file to join to
    Outputs:
        the new, joined shapefile
    
    """
    #simple error checker to make sure the inputs exist
    if not os.path.exists(JoinedFile):
        raise
    if not os.path.exists(inshpfile):
        raise
    #uses geopandas to read the shapefile into a geo-dataframe 
    gdf= geopandas.read_file(inshpfile)
    #uses pandas to read the demography CSV into a regular dataframe
    #You cannot use geopandas for this, unfortunatly
    df= pd.read_csv(JoinedFile)
    # takes the geo-dataframe and joins the dataframe, on common column GISJOIN
    gdf= gdf.merge(df, on ='GISJOIN')  
    #This adds new attribute fields to geo-dataframe for each marker
    #would be three lines or more with loop so kept single
    gdf['pct black'] = (gdf['Black or African American alone']/gdf['Total_y'])*100
    gdf['pct white'] = (gdf['White alone']/gdf['Total_y'])*100
    gdf['pct frgn'] = (gdf['Foreign-Born']/gdf['Total_y'])*100
    
    #This sums all the industry counts for the nation for LQ calculation
    totalPlants = gdf['all industry count'].sum()
    #This sums just the industry counts for the nation for LQ calculation
    total45411xPlants = gdf['45411x industry count'].sum()
    #This creates new field LQ from the national values and the industry count fields
    gdf['LQ'] = (gdf['45411x industry count']/gdf['all industry count'])/(total45411xPlants/totalPlants)
    #exports the modified geo-database to outfile location
    gdf.to_file(outshpfile)    
#function calls for each year, formatted in a loop call
for each in ['2010','2012','2015']:
    JoinStatstoSHP(joinedfilepath +'{}_joined.csv'.format(each), rawfilepath + '{}\\US_zcta_{}.shp'.format(each,each), shpfilepath + '{}File.shp'.format(each))