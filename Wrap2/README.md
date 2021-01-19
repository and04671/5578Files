# GIS5578 Wrapup 2

### Purpose
The purpose of this lab is to help you become comfortable writing code from beginning to end.
Unlike your previous assignments there is no start code.

Choose one (1) of the following tasks and write a Python program that accomplishes it. Use multiple python files if necessary. Choose the task that will demonstrate your knowledge of programming. Be ambitious, but please do not torture yourself. There are no scripts attached but mock has been provided as necessary. Having said that, lecture notes, demos, and labs are sufficient to finish any of the projects below. We have done various elements of this work in class and you should be able to fall back on your previous homework or in-class exercises. 
 
Your code must work and is expected to be efficient, compact but readable, and properly commented. 

### Instructions
1. Please name your file main.py or task(A,B,C).py
1. Please provide a relative directory path for referencing additional files. 
```python
thePath = r"c:\git\myGithHub"
theShapeFilePath = os.path.join(thePath, "shapefiles")
```
###	Your code should
1. Be properly commented
  1. Use proper variable name conventions “snake_case” or “camelCase”
  1. Use descriptive variable names
  1. Should be readable
1. Your code must contain at least one function with the following properties.
  1. A document string 
  1. Comments
  1. Return Statement
1. Use string formatting when appropriate
```python
aName = “Python”
the_variable = 2
print(“Hello World this is {} {}”.format(aName,the_variable ))
```

## Task A
You have been provided a subset of the raster dataset Global Land Cover 2000. The global raster used for comparison is Global Landcover 2000 from the European Space Agency, which is spatial resolution of 0.0089 decimal degree or approximately one square kilometer at the equator.
Information for the dataset can be found at https://lta.cr.usgs.gov/GLCC.

Your task it build a small application that will allow the user to choose the pixel value they would like to have reclassified. The file, GLC2000_legend.csv will provide information about the pixel value associated with each label. You may need to do some preprocessing work to identify if there are any pixel values not present in your dataset and eliminate them. 

1. User should be presented with the labels and values of the raster pixels.
1. User can enter in the value pair, which consists of the current value and the value that they would like it reclassify to.
1. User can enter in any number of value pairs.
1. An empty value pair, starts the reclassification process
1. User specifies the path for new file, reclassified dataset is written to the path as a tiff

## Task B
You have been provided two US datasets, from the National Historic Geographic Information System (NHGIS), which a data project at the Minnesota Population Center at the University of Minnesota. NHGIS contains many of the US publicly release population datasets from 1790 to present day. Your task is to automate a number of tasks that allow you calculate the following things.
### Task B Questions
1. Which county and state have the highest population density?
1. Provide the top 10 counties of nation with the most dense population.
1. Provide the county per state that contributes the most population (in percentage).

For this task you should write code that does the following.
1. Convert CSV to DBF File
  1. Join CSV files to the appropriate shapefiles
  1. US_county_2010.shp
  1. US_state_2010.shp
1. Add new fields (arcpy object) to the shapefile for storing your calculations
1. Uses the arcpy cursor to calculate the new values
1. Population Density per geographic unit (state and county)
  1. Total Population / Area in square kilometer or miles
1.  Fractional of Population Contributed
  1. Population of county / population of state
  1. Population of county / population of country
1. Answer 2 of 3 questions.

## Task C: Raster & Vector Spatial Analysis
Utilize two datasets to complete this task. The first dataset is a subset of the raster dataset Global Land Cover 2000. The global raster used for comparison is Global Landcover 2000 from the European Space Agency. Information can be found at https://lta.cr.usgs.gov/GLCC. The second dataset is from the National Historic Geographic Information System (NHGIS) at the Minnesota Population Center.

For this exercise you will develop an application that automates the raster/vector clipping process. Specifically you will use the arcpy library to extract the raster datasets from a given vector file.  a specific state chosen by the user. us_states.shp file to 

1. The user will be prompted to enter in the name of a geographic feature.
  1. There should be some error checking that informs the user of a potential bad choice and allows them to choose again.
  1. If the user types in “quit” the program quits
1. Your program will select a feature from the existing shapefile 
1. The selected feature will be used to extract the raster data contained within its boundaries.
1. The raster dataset will be written to a tiff with the same file path as the original tiff file.
  1. tiffFilePath = r”c:\work\us_states.tif”
  1. outTiffPath = r”c:\work\Tennessee.tif”
