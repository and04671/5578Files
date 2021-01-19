# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:13:02 2019
@author: Cole
"""
# =============================================================================
import arcpy, os

def CSVJoinToSHP(csvFile, shpFile, csvFolder, dbfFolder):
    """
    Function converts CSV demography files into DBF and then joins to SHP file
        Inputs:
            csvFile: csv demog. file
            shpFile: state or county shapefile
            csvFolder: the folder containing the csvs
            dbfFolder: the temp folder for the dbfs
        Outputs:
            shp file with attached population data
    """
    #this function is best if run just once to avoid duplicate DBFS and joins
    x = input("Have the CSV's already been converted to DBF? [y/n] ")
    #only performs if DBFS have not yet been created
    if x == 'n':
        # joins folder and file into path for csv and shp
        csvPath = os.path.join(csvFolder, csvFile)
        shpPath = os.path.join(shpFolder, shpFile)
        #converts csv path to a DBF and places in dbf folder
        arcpy.TableToDBASE_conversion(csvPath,'dbfs') 
        #defines where the DBF path names are, and their names based on csv file names
        dbfPath = os.path.join(dbfFolder, "{}.dbf".format(csvFile.split(".")[0]) )
        #joins the new DBF to the SHP via GISJOIN column
        arcpy.JoinField_management(shpPath, 'GISJOIN', dbfPath, 'GISJOIN')
#Finds population density for each unit in shpfile  
   
def PopDens(shpFile, shpFolder):
    """
    Function converts CSV demography files into DBF and then joins to SHP file
        Inputs:
            shpFile: state or county shapefile with population data
            shpFolder: the working folder for the shps
        Outputs:
            shp file with attached population data and population density column
    """
    #create shapfile path from folder and file
    shpPath = os.path.join(shpFolder, shpFile)
    # add a population dens field to shpfile *DONT USE [] for ADDFIELD*
    arcpy.AddField_management(shpPath,'pop_dens','FLOAT')
    # create values for each row in shpfile from cursor
    with arcpy.da.UpdateCursor(shpPath,['ALAND10','H7V001','pop_dens']) as cursor:
        for row in cursor:
            # for each pop dens, divide population by land area
            row[2] = row[1]/row[0]
            # finalize values
            cursor.updateRow(row)

def MaxDens(shpFile, maxrows, shpFolder):
    """
    Function finds the rows with maximum density values, number of top values specified
        Inputs:
            shpFile: state or county shapefile with density data
            shpFolder: the working folder for the shps
            maxrows: number of top values to return
        Outputs:
            rows with maximum density
    """
    #dict of storing the max dens rows (cannot use list, need key:variable)
    max_dens = {}
    #empty list to add rows to
    lists = []
    # create shppath from folder and file
    shpPath = os.path.join(shpFolder, shpFile)
    #find the names and pop dens for rows and place in cursor
    with arcpy.da.SearchCursor(shpPath,['NAME', 'pop_dens']) as cursor:
        for row in cursor:
            # add to dictionary, key: row[0], value:row[1]
            max_dens[row[0]]=row[1]        
    #for row, sort top specified keys, append to list in one string
    for key in (sorted(max_dens.keys(), key = max_dens.get, reverse = True )[:int(maxrows)]):
        lists.append('{} {}'.format(key, max_dens[key]))
    #return list of maxes and names
    return(lists)

# =============================================================================
#establish base directory and workspace
startDirectory = r'C:\Users\Cole\Documents\GitHub\wrapup2-and04671'
arcpy.env.workspace = startDirectory
#where each folder is 
csvFolder = os.path.join(startDirectory, 'csv')
shpFolder = os.path.join(startDirectory, 'datasets')
dbfFolder = os.path.join(startDirectory, 'dbfs')

#file calls for county and state file structures
CSVJoinToSHP('nhgis0002_ds172_2010_state.csv', 'us_states_simplified.shp', csvFolder, dbfFolder )
CSVJoinToSHP('nhgis0002_ds172_2010_county.csv', 'us_counties_simplified.shp', csvFolder, dbfFolder)

PopDens('us_states_simplified.shp', shpFolder)
PopDens('us_counties_simplified.shp', shpFolder)

print(MaxDens('us_counties_simplified.shp', 10, shpFolder))
print(MaxDens('us_states_simplified.shp', 1, shpFolder))
# =============================================================================        
#question answers
'''
1. Which county and state have the highest population density?

State: 'District of Columbia 0.0038056098856031895'
County: 'New York County 0.02682190015912056'

2. Provide the top 10 counties of nation with the most dense population.

'New York County 0.02682190015912056'
'Bronx County 0.012703999876976013'
'Queens County 0.007935769855976105'
'San Francisco County 0.0066329101100564'
'Hudson County 0.005301710218191147'
'Suffolk County 0.004793710075318813'
'Los Angeles County 0.0045721400529146194'
'Philadelphia County 0.004393650218844414'
'District of Columbia (County) 0.0038056098856031895'
'Alexandria city 0.003596269991248846'


'''