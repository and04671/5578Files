#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Homework 2 Template
#Shapefile Reader
#GIS 5578
#Fall 2019

### The purpose of this lab is build skills around control structures. ###


### import modules




# In[22]:


### Set the path to the shapefiles
### Set the outcsv path

#so the heck is going on here...you don't need that theDirectory variable
arcpy.env.workspace = r"C:\Users\Cole\Documents\GitHub\lab2-and04671\shapefiles"#print(arcpy.env.workspace)
outFilePath = r"C:\Users\Cole\Documents\GitHub\lab2-and04671\TestCSV.csv"

#**************************************************************************
### This function arcpy.ListFeatureClasses() returns a list of all feature classes found within the geodatabase
# a shapefile is actually an example of a feature class
AllFeatureClasses = arcpy.ListFeatureClasses()
print(len(AllFeatureClasses))
for FeatureClass in AllFeatureClasses:
    print(FeatureClass)
### How will you identify now many feature classes are in the directory?
    #len(AllFeatureClasses) seems to do the trick. There's just 1
### How will you know when there none left?
    #The loop printing each class should stop printing and move on 

### How can you determine which FeatureClass the loop is using?
    #Print the class. It's states.shp

### http://desktop.arcgis.com/en/arcmap/10.3/analyze/python/fields-and-indexes.htm
#so this gets all the fields inside the Feature class    
    for thefield in arcpy.ListFields(FeatureClass):
        print (thefield.name)
#****************************************************************************

### This is extra you can skip this.
### This segment of code will allow you to access the attributes of each field  
### listofFields = This is a variable that is list "object" that contains all the fields of the shapefile
### http://desktop.arcgis.com/en/arcmap/10.3/analyze/python/data-access-using-cursors.htm#ESRI_SECTION1_B52766EB21374F1F9E4727014A9E0A32
##if "Shape" in listofFields: listofFields.remove("Shape")
##if "GEOG" in listofFields: listofFields.remove("GEOG")
##with arcpy.da.SearchCursor(aFeatureClass, listofFields) as cursor:
##  for rec in cursor:
##      #The variables rec is assigned to the first row in the shapefile database
##      for r in rec:
##          #The variable r is assigned to the first object / field in the variable record
##          print(r)
### End of extra stuff ####

### Create a new file
theCSV = open(outFilePath, "w",newline='\n')
for field in arcpy.ListFields(FeatureClass):
    theCSV.write(field.name)
    theCSV.write(", ")
    
### You will need to write out your csv file. 
### Example: theCSV.write("%s, %s" % (field1, field2))
### Example: formattedfields = ",".join( ["field1", "field2", "field3"]  )

theCSV.close()
### Make sure to close your file

