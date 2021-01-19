
# The following script uses a class to calculates a statistics based
# on a predefined 2-dimensional array (grid)
#
# SKILLS:
#       1. using a numpy array 
#       2. defining functions
#       3. using functions
#
# Author: David Haynes
#
#------------------  Modules loaded -----------------
#
#
#
#
#
##    
##
##---------------ITEMS MISSING
##        
##
##-------------
def getRowStatistics(theData):
    """returns the row stats for the numpy object"""
    #Need to add additional statistics
    theRow = theData[row,:]
    return theRow.sum()

##def changeCellValue(row,column,newvalue):
##'This function will allow you to change a cell value'
##pass



# Use this as a test for the user defined list
mygrid = [[2,3,5],[1,2,6],[3,4,2]]
##


##
##
##This converts the list to a grid.
#grid = np.array(mygrid, dtype=np.float)

print('')
print('here is the sum of that row: %s' % (getRowStatistics(grid, 0))


