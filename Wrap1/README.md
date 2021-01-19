# GIS5578 WrapUp 1

### Purpose
The purpose of this lab is to help you become comfortable writing code from beginning to end.
Unlike your previous assignments there is no start code.

Choose one (1) of the following tasks and write a Python program that accomplishes it. Use multiple python files if necessary. Choose the task that will demonstrate your knowledge of programming. Be ambitious, but please do not torture yourself. There are no scripts attached but information as possible has been provided as necessary. Having said that, lecture notes, demos, and labs are sufficient to finish any of the projects below. We have done various elements of this work in class and you should be able to fall back on your previous homework or in-class exercises. 
 
Your code must work and is expected to be efficient, compact but readable, and properly commented. 

### Instructions
1. Please name your file main.py or task(A,B,C).py
1. Please provide a relative directory path for referencing additional files. 

```python
import os
thePath = r"c:\git\myGithHub"
theShapeFilePath = os.path.join(thePath, "shapefiles")
```

## Task A
Write a script that takes coordinates of multiple points from the user and calculates the total Euclidean distance between subsequent pairs of points (i.e., line segments). The use story is as follows: 
1. The user specifies the number of points they want to input (e.g., 3). 
1. Sequentially, for each point, the user enters its coordinates, for example, (x1, y1), (x2, y2), (x3, y3) or x1, y1, x2, y2, x3, y3. 
3. Your code calculates the distance from point Pk to the consecutive point Pk+1 (e.g., from point P1 to point P2, from P2 to P3; see figure 1). 
1. The total distance (Total_d) is derived by summing up the lengths of the individual line segments 
(e.g., Total_d = dP1P2 + dP2P3). 
1. The total distance is displayed to the user in a descriptive manner. 
1. Make sure that your code works for any number of points (e.g., 0, 1, 10, 100+). 

## Task B
Write a script that generates and saves a random integer ASCII grid based on a user-specified size and range. The use story is as follows: 
1.  The user specifies the number of columns and rows for the raster to be generated (e.g., 4 cols and 5 rows). 
1.  Then, the user specifies the range and step of values to pool from when populating the grid values (e.g., from 2 to 8 with step of 2 which results in the following set of integers: 2, 4, 6, 8; see next step).  
1.  Based on the input, the system generates a 2-dimensional array of a given size and then populates it with values randomly (!) selected from the pool of eligible integers (as described above; see figure 2 for an illustration). 
1.  The array is saved to a text or comma separated csv file without the header. 


## Task C
Write a simple spatial calculator, which takes two ASCII grid files from the user (sample data are attached), performs a user-specified calculation on them, and saves the result to a file in the ASCII grid file format. The use story is as follows: 
1. The user specifies the name and path of the input ASCII grid files (with a separate path for each of the input files)  
1. The script checks if the two grids are of the same size (same number of columns and rows). If not, then the system displays an error message and either quits or loops until the user specifies a second ASCII file with grid of the same size as the first one).  
1. The user is asked about what type of operation to perform on the input grids. Provide the following options: sum, difference, multiplication, and division. For division, make sure that you do not divide by zero (in this case assign a NoData value to the output; see figure 3).  
1. The script performs the selected local operation (i.e., cell-by-cell map algebra operation) and saves the result back to an ASCII grid file (excluding the ASCII file header).  



