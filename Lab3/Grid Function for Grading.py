#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The following script uses a class to calculates a statistics based
# on a predefined 2-dimensional array (grid)
# SKILLS:
#       1. using a numpy array 
#       2. defining functions
#       3. using functions
# Author: Cole Anderson
#------------------  Modules loaded -----------------
import numpy as np
import csv
#outer directory and list of CSVs for program
Directory = r"C:\Users\Cole\Documents\GitHub\lab3-and04671"
CSVs = [r"\random_values",r"\one_zero"]


# In[26]:


#-------------Functions Loaded---------------------------------------------
def RowStatistics(InputGrid,row):
    """returns stats for the desired numpy row object"""
    theRow = InputGrid[row,:]
    return(getArrayStats(theRow))
def ColStatistics(InputGrid,col):
    """returns stats for the desired numpy column object"""
    theCol = InputGrid[:,col]
    return(getArrayStats(theCol))   
def getArrayStats(Array):
    """this is called from the other functions to execute and return stats"""
    return("sum:",np.sum(Array),"average:",np.average(Array),"standard dev:",np.std(Array))   
def changeCellValue(InputGrid,row,column,newvalue):
    '''this function will find and replace a value at an index with another'''
##'This function will allow you to change a cell value'
    InputGrid[row,column] = newvalue


# In[27]:


##script for finding desired row/column in files
desiredRow = 7
desiredColumn = 6
##-------------------------------------------
#will find row/col stats for both files
for CSV in CSVs:
    #combine path and create list from CSV
    completePath = Directory + CSV +".csv" 
    with open(completePath, "r") as csvFile:
        listFromCSV = list(csv.reader(csvFile))
    #create array from list
    gridFromList = np.array(listFromCSV, dtype=np.float)
    #optional change value call
    #changeCellValue(gridFromList,3,5,1)
    #print stats
    print("File:", CSV)
    print("   Row Statistics for row",desiredRow,":",RowStatistics(gridFromList,desiredRow))
    print("   Column Statistics for column",desiredColumn,":", ColStatistics(gridFromList,desiredColumn))


# In[28]:


#similar to above. opens all CSVs and converts them to array, then finds stats for whole file
for CSV in CSVs:
    completePath = Directory + CSV +".csv" 
    with open(completePath, "r") as csvFile:
        listFromCSV = list(csv.reader(csvFile))
        #listFromCSV = [[2,3,5],[1,2,6],[3,4,2]]
    gridFromList = np.array(listFromCSV, dtype=np.float)
    print(completePath,"\ninitial stats:",getArrayStats(gridFromList))
#--------------------------------------------
#this should count all the eights, and replace all 8s in the grid with 2
    print("number of eights in array:", np.count_nonzero(gridFromList==8))
    gridFromList[gridFromList==8] = 2
    print("all eights are now twos")
    
    #stuff I tried
        #x = np.where(gridFromList == 8)
        #print(x)
        #if (len(x[0]) or len(x[1]))==0:
           # print("yikes, no eights")
            #continue
        #else:
            #for each in x:
             #   print(each)
                #print([0])
                #changeCellValue(gridFromList,eights[0],eights[1],2)
#--------------------------------------------    
    #prints the new array stats after replacement
    print("new statistics:",getArrayStats(gridFromList),"\n")
    

