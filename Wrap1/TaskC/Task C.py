# -*- coding: utf-8 -*-
"""
TASK C
@author: Cole Anderson

Score 45/50
The code is pretty good. You missed one item. None of your functions were returning anything

"""

import numpy as np
import os

# =============================================================================
# Specify relative directory paths
directoryBase = r"C:\git\GIS5578_fall_2018\lab-grading\wrapup1\wrapup1-and04671\TaskC"
asciiFile1 = r"rasterA.txt"
asciiFile2 = r"rasterB.txt"


# =============================================================================
#Functions
def pathJoinToArray(relPath,directory):
    """
    Function does following:
    
    Joins the directory and file into full path, and opens the ASCII file
    turns ASCII file into list of lists of integers by line splits
    turns list into np.array and returns it
    """
    fullPath = os.path.join(directory,relPath)
    with open (fullPath,"r") as file:
           results = []
           for eachLine in file:
               values = [int(each) for each in eachLine.split()] 
               results.append(values)
    print(results)
    arrayFile = np.array(results)
    return arrayFile 

def sumValues(a1,a2):
    """
    summing with np is easy, specify arrays as args in np.add
    prints resultant array
    """
    x = np.add(a1,a2)
    print(x)
    return x
    
def multValues(a1,a2):
    """
    multiplication requires arrays to multiply as args in np.multiply
    prints resultant array
    """
    x = np.multiply(a1, a2)
    print(x)
    return x

def divValues(a1,a2):
    """
    function np.divide requires divisor and dividend
    these are specified using user input
    print resultant array
    """
    #user picks which array is divisor
    divisor = input("Specify divisor array (array1 or array2): ")
    #set the program to ignore divide by zero errors (replaces with inf)
    np.seterr(divide = 'ignore')
    #plugs in array args as desired by user
    if divisor == "array1":
        x = np.divide(a2,a1) 
    elif divisor == "array2":
        x = np.divide(a1,a2) 
    #changes type inf to none as instructed
    x[x == np.inf] = None
    print(x)
    return x

def subValues(a1,a2):
    """
    function np.subtract requires user input specified subtrahend
    print resultant array
    """
    #user picks which array is subtracted
    subtrahend = input("Specify subtrahend array (array1 or array2): ")
    #plugs in array args as desired by user
    if subtrahend == "array1":
        x = np.subtract(a2,a1) 
    elif subtrahend == "array2":
        x = np.subtract(a1,a2)
    print(x)
    return x
# =============================================================================
#Function Calls
    
#these take the input ASCII, attach them to the directory base
#then turn ASCII into NP Arrays
array1 = pathJoinToArray(asciiFile1, directoryBase)
array2 = pathJoinToArray(asciiFile2, directoryBase)

#This clarifies which array is which ASCII for the user
#So they can select the correct ones
print("array1 is:\n",array1,"\n")
print("array2 is:\n",array2)

#This checks that the shapes of the arrays are not different
if(array1.shape != array2.shape):
    print("The arrays you have specified are not the same size")
    #exit program if different
    exit
    
#Asks user for preferred operation from given  
operation = input("select operation: sum, difference, multiplication, division ")
#checks for each response in turn and runs appropriate function call
if operation == "sum":
    x = sumValues(array1,array2)
elif operation == "multiplication": 
    x = multValues(array1,array2)
elif operation == "difference":
    x = subValues(array1,array2)     
elif operation == "division":
    x = divValues(array1,array2)
#if the response is not exactly one of those things, exit program
else:
    print("Not a valid operation")
    exit
    
#This cool one liner writes the new array x to new file
print("Saving to new file grid\n")
#Spinning, that's a good trick
np.savetxt("rasterout.txt", x, fmt='%f')
#Doc for above op: https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html
# =============================================================================
    


    

   
