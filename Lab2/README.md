# GIS5578 Homework 2


### Purpose
The focus of this lab is get more experience using control structures (if-else-elif) and to improve code generalization and reduce errors. Student should write code that contains for loops and if then statements when necessary.


## Assignment 1: Shapefile Reading
As a GIS developer you will often make scripts that start off with a small single purpose. However, you will often find that those scripts can be modified to serve additional purposes with little modification. Write a Python script for the following scenario. 

Your script will be tested on a directory with at least three shapefiles. Each shapefile will have a different number of attributes.

You have been provided a script template that has helpful formatting. Your goal is to write a script that can read one or more shapefiles that are in the same directory. The script should read all of the datasets and then write out to a (CSV) file each field and all of the attributes found in the shapefile. It is not required or recommended that you use the csv module, simply writing out a comma separated file with a txt file extension is enough. The output file should load into excel.

### Optional 
Please to go data.terrapop.org and make a new user account. Create at least two area-level extracts for testing purposes. The area-level extracts will be the basis for your data for this homework assignment. Start out with a small extract that has two or three variables. Verify that your script works and then make a larger extract with more variables. The objective of your script is generalization. The script will read a user directory with 1 or more shapefiles and output information. 

### Here are the general steps that you should take. 
1. Import the arcpy module
1. Set a variable to the path of shapefiles 
1. Set a variable to the outcsv path
1. Get the All the FeatureClasses in the 
1. Get a single FeatureClass
1. Find all the fields in the FeatureClass
1. Use the SearchCursor
1. Use string methods like replace and slicing to format the string
1. Write the string to a file
1. Close the file

Note: You may write all information out to a single file. The output format is not important.


## Assignment 2: Raster Generation Automation Tool

Much of today’s complex geospatial analyses are done using raster datasets. However, raster datasets come in over 100 different formats. As a GIS analyst you will often need to convert a dataset from one format to another. Your task to write a script that automates the data conversion process. There are three csv files which contain different raster datasets. Your task is to write a script that converts them into geotiffs. You will use the ESRI ASCII to Raster_Conversion function to create the dataset.

### Here are the general steps that you should take
1. Read the csv file
1. Write the asc file
  1. Write the header
  1. Write the data without commas
1. Uses the arcpy module to convert each file into a geotiff
