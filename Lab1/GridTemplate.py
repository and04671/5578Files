# The following script calculates a number of statistics based
# on a predefined 2-dimensional array (grid)
#
# SKILLS:
#       1.looping
#       2.the 'list' object
#       3.built-in functions
#       4.module importing
#
# Author: David Haynes
 
# INPUT MATRIX------------------
grid = [[1,1,2,4,1,7,1,7,6,9],\
        [1,2,5,3,9,1,1,1,9,1],\
        [7,4,5,1,8,1,2,0,0,4],\
        [1,4,1,1,1,1,1,1,8,5],\
        [9,0,0,0,0,0,1,1,9,8],\
        [7,4,2,1,8,2,2,2,9,7],\
        [7,4,2,1,7,1,1,1,0,5],\
        [3,4,5,3,4,5,9,1,0,9],\
        [0,0,5,1,1,1,9,7,7,7]]

print('')
print("Our grid *********************")

for i in grid:
   print(i)
        
# SIZE OF MATRIX ---------------
# row num
# col num
# cell num


print("\n Number of rows", rows)
print("\n Number of cols", cols)
print("\n Number of cells", celNum)


# ****** PUT YOUR CODE HERE **********
# Hint: the easiest way to calculate
# the stats is to convert the
# 2D grid into a 1D array (list)
# ************************************

# ************* PUT YOUR CODE HERE *************
# Use the 'enumerate' function to display the row id/index and the
# corresponding row values for all rows in the grid
# You will need to research how the enumerate function works
# Use the enumerate funtion on your grid to determine a column from a 2D grid
# Convert the values to a list, which can be converted to a numpy array


# USER SELECTED ROW -----------------
rowID = 1 # hard-coded user input for testing make sure you change this

# What does the following if-clause do?
# Expand this to include columns
if rowID > rows - 1 or rowID < 0:
    print("Row index out of range")
    print("Setting to default -> the 1st row")
    rowID = 0
    
selectedRow = grid[rowID]

print("row", rowID, "values:",)
print(selectedRow)


# ****** PUT YOUR CODE HERE **********
# Calculate the sum and average
# and display (ie. print) the values
# with some text that tells the user
# what value s/he is looking at;
# similarly, calculate the min, max,
# and range of values within grid;
# there are quite a few built-in list
# functions that can make your life
# easy
# CALCULATE AND print(SUM ------------
# CALCULATE AND print(AVERAGE --------
# CALCULATE AND print(MIN ------------
# CALCULATE AND print(MAX ------------
# CALCULATE AND print(RANGE ----------
# ************************************

#HINT
#print(maxvalue


# Extra have a user input a row and column number return the value
# SELECTED ROW/COL -------------
inCol = 9  # X coord - user input
inRow = 8  # Y coord - user input


# ************* PUT YOUR CODE HERE *************

selCell = 0 # retrieve the correct value


print("cell (" + str(inRow) + "," + str(inCol) + ") value:",)
print(selCell)
print(grid[selCell])

