# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:41:56 2019

@author: Cole
"""
# =============================================================================
# Import Modules
# =============================================================================
import csv
from collections import OrderedDict
import pandas as pd
import geopandas
# =============================================================================
#Function Definitions
# =============================================================================
#Gather and furnish variable dictionary from codebook file

def ReadDataDictionary(infilePath):
    """
    This function reads the data dictionary codebook.
    It looks for the colon in each record and then splits into varKey and varFullName
    
    Example below:
    MSA_CMSAA:   Metropolitan Statistical Area/Consolidated Metropolitan Statistical Area Code
    Key : Value
    """  
    #opens the codebook file and splits at new line characters
    with open(infilePath) as f:
        data = f.read().split("\n")
        #establishes an empty dictionary to put translation of abbreviations in
        #Question: would there be an advantage to an ordered dictionary here?
        variableDictionary = {}
        
        for line in data:
            if ":" in line:
                # strips off everything on the line AFTER the colon and assigns
                varKey = line[ :line.find(":")].strip()
                # and this strips off everything BEFORE the colon and assigns
                variableName = line[line.find(":")+1: ].strip()
                variableDictionary[varKey] = variableName
                #print(variableDictionary)
    #now, there are entries in the dictionary that won't really do anything for the renaming
    #is it best practice to just leave it that way?                            
    return variableDictionary

def ParseMultipleDictionaryOccurences(theDict):
    """
    Sometimes the metadata file will result in similar names that are not unique.
    We want to make them all unique
    """
    #per capita income in 1999 has duplicate ['Table 2', 'GNW001']
    from collections import Counter
    #Use the counter to get all the full variable names which are not unique
    #Get the values from the dictionary, convert to a list and use the counter
    valueList = list(theDict.values())
    values = Counter( [v.lower() for v in valueList] )
    
    #For each full variable name find those that have duplicates
    for v in values:
        if v and values[v] > 1:
            #print("%s has duplicate" % (v))
            #Create a list of the original keys, which are unique so you can get there non-unique key names
            duplicates = [k for k in theDict if theDict[k].lower() == v.lower()]
            #print(duplicates)
            for c, d in enumerate(duplicates):
                #igore the zero column, basiscally add _1 or _2 to the duplicates
                if c: 
                    theDict[d] = "%s_%s" % (v.lower()[:61], c)   
    return theDict

def ReadCSV(theCSVPath, variableDict, thePrimaryKey="FID"):
    """
    This function reads in the data csv and keeps it in its original format using OrderedDict
    Specify the primaryKey = "ObjectID"
    
    The nesting structure is annoying but useful
    
    Create a list of tuples for each field [ (fieldName, fieldValue) ....]
    
    This preserves the order of the attributes, mostly important when writing the data out
    OrderedDict( [(field, line[field]) for field in fieldnames] )
    
    These are packed together into another OrderedDictionary perserving the row order
    OrderedDict( (int(line[thePrimaryKey]),  OrderedDict( [(field, line[field])
    """     
    with open(theCSVPath, "r") as inFile:
        theReader = csv.DictReader(inFile, delimiter=",")
        #these are just the header names
        fieldnames = theReader.fieldnames
        #return(fieldnames[4])       
        #but what does this do?
        outDataset = OrderedDict( (line[thePrimaryKey],  OrderedDict( [( variableDict[field], line[field]) for field in fieldnames] )  ) for line in theReader )
        #but I gather the variable Dict has somehow been related to the data dict...or something
        return outDataset

def WriteFile(filePath, theDictionary):
    """
    This function writes out the dictionary as csv
    """   
    thekeys = list(theDictionary.keys())   
    with open(filePath, 'w', newline='\n') as csvFile:
        fields = list(theDictionary[thekeys[0]].keys())
        theWriter = csv.DictWriter(csvFile, fieldnames=fields)
        theWriter.writeheader()

        for k in theDictionary.keys():
            theWriter.writerow(theDictionary[k])           
    
def JoinDemoToIndustry(ZCTAFile1, ZCTAFile2, ZIPFile, JoinedFile):
    """
    This function takes all of the relavent csvs and joins them via GISJOIN
    """
    
    ZCTA1_csv = pd.read_csv(ZCTAFile1)
    ZCTA2_csv = pd.read_csv(ZCTAFile2)
    #Both ZIPS
    ZIP_csv = pd.read_csv(ZIPFile, dtype = {'zip':str}) 
    ZIP_csv = ZIP_csv[['zip','naics','est']]
    ZIP_csv['zip'] = ('G' + ZIP_csv['zip'])
    #ZIP1, the industry specific counts
    ZIP1_csv = ZIP_csv[(ZIP_csv.naics == '454110') |
                      (ZIP_csv.naics == '454111') |
                      (ZIP_csv.naics == '454112') | 
                      (ZIP_csv.naics == '454113') |
                      (ZIP_csv.naics == '454114') | 
                      (ZIP_csv.naics == '454115') |
                      (ZIP_csv.naics == '454116') | 
                      (ZIP_csv.naics == '454117') |
                      (ZIP_csv.naics == '454118') | 
                      (ZIP_csv.naics == '454119')]
    #now, add the nxxx_xxx values together for for rows with any of those numbers for a ZIP
    ZIP1_csv = ZIP1_csv.groupby('zip').sum()
    ZIP1_csv = ZIP1_csv.reset_index()
    ZIP1_csv = ZIP1_csv.rename({"est":"45411x industry count"},axis = 1)
    #ZIP2, the total counts
    ZIP2_csv = ZIP_csv
    ZIP2_csv = ZIP2_csv.groupby('zip').sum()
    ZIP2_csv = ZIP2_csv.reset_index()
    ZIP2_csv = ZIP2_csv.rename({"est":"all industry count"}, axis = 1)
    #merge ZCTA demo files
    #only want keys we can do ALL tests on (how=inner)
    ZCTAmerge = ZCTA2_csv.merge(ZCTA1_csv, on ='GIS Join Match Code')
    ZCTAmerge = ZCTAmerge.dropna(axis = 1, how='all')
    #merge ZIP industry files
    
    #we want to make sure to preserve all ZIPs, even ZIPs with no 45411x (how = outer) 
    
    ZIPmerge = ZIP2_csv.merge(ZIP1_csv, how = 'outer',on = 'zip')
    #but those areas with no 45411x need to be labeled '0' for that column
    ZIPmerge = ZIPmerge.fillna(0)
    #print(ZIPmerge)
    
    #merge the previous merges
    #we only want the zip/zcta overlap (ie, no data point if missing demo or industry)(how=inner)
    final = ZIPmerge.merge(ZCTAmerge, left_on ='zip', right_on = 'GIS Join Match Code')
    final = final.rename({'GIS Join Match Code':'GISJOIN'},axis = 1)
    final.to_csv(JoinedFile)
   
def JoinStatstoSHP(JoinedFile, inshpfile, outshpfile):
    gdf= geopandas.read_file(inshpfile)
    df= pd.read_csv(JoinedFile)
    gdf= gdf.merge(df, on ='GISJOIN')
    gdf['pct black'] = (gdf['Black or African American alone']/gdf['Total_y'])*100
    gdf['pct white'] = (gdf['White alone']/gdf['Total_y'])*100
    gdf['pct frgn'] = (gdf['Foreign-Born']/gdf['Total_y'])*100
    totalAllPlants = gdf['all industry count'].sum()
    total45411xPlants = gdf['45411x industry count'].sum()
    gdf['LQ'] = (gdf['45411x industry count']/gdf['all industry count'])/(total45411xPlants/totalAllPlants)
    gdf.to_file(outshpfile)
# =============================================================================
#Calls and Processing
# =============================================================================
directory = r"C:\Users\Cole\Documents\GitHub\class-project-and04671\\"
rawfilepath = directory + 'Raw\\'
joinedfilepath = directory + 'Joined\\'
shpfilepath = directory + 'SHP Files\\'


demogFiles = [
 "ZCTA 2008-12 Nativity E",
 "ZCTA 2008-12 Race and Income E",
 "ZCTA 2010-14 Nativity E",
 "ZCTA 2010-14 Race and Income E",
 "ZCTA 2013-17 Nativity E",
 "ZCTA 2013-17 Race and Income E"]

industryFiles = [
 "zbp10detail",
 "zbp12detail",
 "zbp15detail"]

#graps files in RAW and cleans them
for file in demogFiles:
    extractFileName = file
    extractCodeBookFileName = file + " Codebook"
    #this is the codebook path
    codebookFilePath = rawfilepath + "{}.txt".format(extractCodeBookFileName)
    #this is the extract CSV path
    extractFilePath = rawfilepath + "{}.csv".format(extractFileName)
    #this is where the CSV with new header goes
    extractFilePath_new = rawfilepath + "{}_clean.csv".format(extractFileName)
    #this is the codebook functions call
    codebookVariableDict = ParseMultipleDictionaryOccurences(ReadDataDictionary(codebookFilePath))
    #and this is the datasheet function call
    datasetDictionary = ReadCSV(extractFilePath, codebookVariableDict, "GISJOIN")
    #takes the dictionary of dataset values and the 
    WriteFile(extractFilePath_new, datasetDictionary)

#joins cleaned files to industry files and  spits out joined file into Joined folder
JoinDemoToIndustry(rawfilepath + 'ZCTA 2008-12 Nativity E_clean.csv', rawfilepath + 'ZCTA 2008-12 Race and Income E_clean.csv', rawfilepath + 'zbp10detail.txt',joinedfilepath +'2010_joined.csv')
JoinDemoToIndustry(rawfilepath + 'ZCTA 2010-14 Nativity E_clean.csv', rawfilepath + 'ZCTA 2010-14 Race and Income E_clean.csv', rawfilepath + 'zbp12detail.txt',joinedfilepath +'2012_joined.csv')
JoinDemoToIndustry(rawfilepath + 'ZCTA 2013-17 Nativity E_clean.csv', rawfilepath + 'ZCTA 2013-17 Race and Income E_clean.csv', rawfilepath + 'zbp15detail.txt',joinedfilepath +'2015_joined.csv')

JoinStatstoSHP(joinedfilepath +'2010_joined.csv', rawfilepath + '2010\\US_zcta_2010.shp', shpfilepath + '2010File.shp')    
JoinStatstoSHP(joinedfilepath +'2012_joined.csv', rawfilepath + '2012\\US_zcta_2012.shp', shpfilepath + '2012File.shp') 
JoinStatstoSHP(joinedfilepath +'2015_joined.csv', rawfilepath + '2015\\US_zcta_2015.shp', shpfilepath + '2015File.shp') 






