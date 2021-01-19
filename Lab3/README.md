# GIS5578 Lab 3

### Creating Functions


### Purpose
The focus of this lab is to students the basic principals necessary for developing their own functions. Functions are the first step to learning object orientated programming. Functions are generalized pieces of code that accomplish a particular task. The students should develop functions to accomplish the identified tasks and learn how to use them appropriately.
Take the statements you used in Python from the exercise in week one and modify your code so that is uses functions for determining the statistics for a row or column. You may use the given script grid_function_template.py as a guide. I do expect you to create your own script outside of the template. There is some helpful information within the template that should point you in the correct direction. Start by making your code as verbose, clear, and simple as possible. In the template, I noted the lines where your code should be put, but remember to make the script your own.

### Directions
1. Write a script to process the following inputs of data
* Using a user defined list **
* Using the one_zero.csv
* Using the random_values.csv


2. Create the following functions
* Find the average, sum, standard deviation for a row
* Find the average, sum, standard deviation for a column
* For the file(s)
  * Find the average, sum, standard deviation for the file
  * Count the number of occurrences of ‘8’
  * Replace the value ‘8’ with 2 your dataset
* Recalculate all the statistics
* Read a CSV through a function

3. Proper documentation
* Functions should have doc strings

```
def getRowStatistics(theData):
    '''This is a function doc stri1ng, returns row stats for the numpy object'''
    theRow = theData[row,:]
    return theRow.sum()
```

* Remember to use consistent variable names
* Remember to use comments appropriately

4. The script should be automated and utilize all the functions that you have built.
5. Be sure to include a statements that call your functions for the built in list or a csv.
