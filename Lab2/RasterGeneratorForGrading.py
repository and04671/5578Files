#!/usr/bin/env python
# coding: utf-8

# In[227]:


#Homework 2 Template
#Raster Generating Script
#GIS 5578
#Fall 2019
#
###Cole Anderson
#
# Score 10/10
# Comments: the code is good. Try to think about restructuring your code if you notice your are copying and pasting

### import modules
import arcpy
import csv 

#establish designated file paths. CHANGE FOR EACH FILE
arcpy.env.workspace = r"C:\Users\Cole\Documents\GitHub\lab2-and04671"
csvFilePath = r"csv_files\mn_counties.csv"
ascFilePath = r"asc_files\mn_counties.asc"

#A little magic you can use or you can split it into two separate with statements
with open(csvFilePath, "r") as fileIn, open(ascFilePath, "w",newline='\n') as fileOut:
    #opens the fileIn as a delimited dataset
    dataset = csv.reader(fileIn, delimiter=',')
    
    #listDataSet = list(dataset)
    #print(x[1])
    #huh..as soon as I put that test in there it fails
    #dataset is a csv object that has a built in iterator. 
    # I think you would need to cycle through it newlist=[d for d in dataset] 
    #x= list(dataset)
    #print(x[1][1])
#*****************************************************************
#To start with, what are the metadata for the csv file?
#CHANGE THIS FOR EACH FILE
#I literally just counted the rows and columns in the CSV file.
#Will build autocounter if time
    #GLC    
    #NCOLS = 868
    #NROWS = 659
    
    #MN or MNCOUNTIES
    NCOLS = 867
    NROWS = 659
    
    #ALL
    XLLCORNER = -97.239209 
    YLLCORNER = 43.499356
    CELLSIZE = 0.0089285714000
    NODATA_VALUE = -99
#*****************************************************************
#under the hood
#this puts the designated values into strings for writing to fileOout
    formattedNCOLS = "NCOLS"+ " " + str(NCOLS) + "\n"
    #formattedNCOLS = "NCOLS {}\n".format(NCOLS)

    formattedNROWS = "NROWS"+ " " + str(NROWS) + "\n"
    formattedXLLCORNER = "XLLCORNER"+ " " + str(XLLCORNER) + "\n"
    formattedYLLCORNER = "YLLCORNER"+ " " + str(YLLCORNER) + "\n"
    formattedCELLSIZE= "CELLSIZE"+ " " + str(CELLSIZE) + "\n"
    formattedNODATA_VALUE = "NODATA_VALUE"+ " " + str(NODATA_VALUE) + "\n"
#Writes header to fileOut  
#Abstract things that are copied and pasted
for f in [frmattedNCOLS, formattedNROWS...]
    fileOut.write(f)

    fileOut.write(formattedNCOLS)
    fileOut.write(formattedNROWS)
    fileOut.write(formattedXLLCORNER)
    fileOut.write(formattedYLLCORNER)
    fileOut.write(formattedCELLSIZE)
    fileOut.write(formattedNODATA_VALUE)
#These are some row and item counters used for testing
    outercounter = 0
    innercounter = 0
#these nested loops write the dataset to fileOut. Had trouble with this   
    #for each ROW in the dataset
    # Does something like this work?
    # " ".join(row)
    for row in dataset:
        #for each NUMBER in that row
        for number in row:
            #so this is item plus space to seperate the values
            number = number + " "
            #adding to the counder for tracking
            innercounter=innercounter+1
            #writes the number, as a string, to fileOut
            fileOut.write(str(number))
        #adding to the counter for tracking
        outercounter=outercounter+1
        #IMPORTANT: new line at the end of row loop
        fileOut.write("\n")
#*************************************************************
#some other stuff I tried to convert to ASC
        #for item in row:
         #   print(len(item))
            
    ### Write all the data
    #theWriter = csv.writer(fileOut, delimiter =',')
    #for row in dataset:
     #   print("yes")
      #  theWriter.writerow(row) #This is not correct
      #  print(row)
    
### Convert Asc File to geotiff
### http://pro.arcgis.com/en/pro-app/tool-reference/conversion/ascii-to-raster.htm


# In[228]:


#same here.CHANGE FOR EACH FILE
outraster = r"C:\Users\Cole\Documents\GitHub\lab2-and04671\TIFF_files\mn_counties.tif"
ascFilePath = r"C:\Users\Cole\Documents\GitHub\lab2-and04671\asc_files\mn_counties.asc"

arcpy.ASCIIToRaster_conversion(ascFilePath, outraster, "INTEGER")

