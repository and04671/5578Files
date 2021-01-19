import csv
import numpy as np

class grid(object):
    """
    Class turns file into data array and calculates the mean,min, max for 
    entire array or specified row/column
    
    Parameters:
        init requires filepath: path to desired file
        user input to row/col functions
    Returns:
        stats for desired array, row, or column
    """
# =============================================================================
# Initiation and Data Functions    
# =============================================================================
    def __init__(self, inputdata):
        """
        Initiates instance of class object 
        Calls to data_loader for data attricbute
        Assigns shape and size attributes to self
            
        Parameters: 
            inputdata: str filepath to data file
        """
        #instance used data loader to assign data attributes
        self.data = self.data_loader(inputdata)
        self.shape = self.data.shape
        self.rows, self.cols = self.shape
        #attribute height/width defined as index of shape attribute
        self.height= self.shape[1]
        self.width= self.shape[0]

    def data_loader(self, inputdata): 
        """
        Loads csv or list data files into object instance as array. Calls to convert_CSV
        function if file is str instance, posts error message if neither list/str
        
        Parameters: 
            inputdata: str filepath to data file entered in initial call
        Returns:
            data: list form of inputdata file
        """
        #if the input data is a list
        if type(inputdata) == list:
            #turns list directly into np array, type int
            data = np.array(inputdata, dtype=np.integer)
            #self.data = np.array(inputdata)
            #inputdata is a list
        #if the input is a string
        elif isinstance(inputdata, str):  
            #runs convert to list, then to np array. type int. (this was where I had issues)
            data = np.array(self.convert_CSV_to_list(inputdata), dtype=np.integer)
        #anything else, error message
        else:
            print("invalid data type")
        #spit out data into class
        return data

    def convert_CSV_to_list(self, filepath):
        """
        Called in case filepath format is str (CSV is axample)
        Uses csv reader to read into list
        
        Parameters: 
            filepath: generic str filepath to data file
        Return:
            outdata: list form of CSV
        """
        outdata = []
        #open file path and run csv reader, add to list row by row
        with open(filepath, 'r') as fin:
            reader = csv.reader(fin)
            #outdata = list[reader]
            for row in reader:
                outdata.append(row)
        #spit data out to data loader
        return outdata
# =============================================================================
# Calculation Functions    
# =============================================================================

    def grid_statistics(self):
        """
        Uses instance data atttribute to call to array_stats function
        Ultimatly displays numerical stats for file
        
        Parameters:
            none
        Return:
            none (on its own, array_responsible for print/return)
        """
        #set x equal to a run of array_stats on data attribute
        x = self.array_statistics(self.data)
        #print(x)
    def get_input(self, phrase, ):
        """
        Requests input from user based on parameter phrase
        
        Parameters:
            phrase: question to user, column or row request in this case
        Returns: 
            value: variable containing user answer
        """
        #requests input based on phrase and records
        value = input(phrase)
        return value
    
    def array_statistics(self, theArray):
        """
        Actual calculation of statisics for parameter theArray, prints and returns
        min,max,mean
        
        Parameters:
            theArray: np.array of input data file
        Returns:
            theMin, theMax, theMean: calculated array statistics
        """
        #calculates stats of input array
        theMin = theArray.min()
        #heMin = np.min(theArray)
        theMax = theArray.max()
        #theMax = np.max(theArray)
        theMean = theArray.mean()
        #theMean = np.average(theArray)
        #prints/returns results
        print(theMin, theMax, theMean)
        return theMin, theMax, theMean

    def getRowStats(self,):
        """
        Calls user to input row number and uses array_stats to calculate for row
        
        Parmeters: none direct, 
        Returns: 
            self.array_stats(theArray): calculation fo row stats
        """
        #row is int of get_input request for row number
        row  = int(self.get_input("Please enter the row: "))
        #makes sure row value is less than number of rows, greater than zero
        if row >= 0 and row <= self.rows:
            #the array becomes just the row of the data
            theArray = self.data[row,:]
            #runs array_stats on just that row
            return self.array_statistics(theArray)
        #if not valud row, error message
        else:
            print("Entered an in invalid value")
            
            
    def getColStats(self,):
        """
        Calls user to input column number and uses array_stats to calculate for column
        
        Parmeters: none direct, 
        Returns: 
            self.array_stats(theArray): calculation fo row stats
        """
        #row is int of get_input request for col number
        col  = int(self.get_input("Please enter the column: "))
        #makes sure col value is less than number of cols, greater than zero
        if col >= 0 and col <= self.cols:
            #the array becomes just the cols of the data
            theArray = self.data[:,col]
            #runs array_stats on just that col
            return self.array_statistics(theArray)
        #if not valud col, error message
        else:
            print("Entered an in invalid value")
         
a =grid(r'random_values.csv')
print(a.shape)
print(a.height)
print(a.width)
a.grid_statistics()
a.getRowStats()
a.getColStats()

'''
Homework Questions:

1. In your own words define a class or object:
    *A class/object is a data structure that defines the operations and attributes for an instance, but is itself only a frame.

1. In your own words define an instance of an object:
    *An instance of an object is a particular memory occurence build on a class framwork. Its attributes can be specifically called

1. What methods run after the mygrid class is initiated?
    Methods: __init__, data loader, CSV_to_list IF file is instance of type string

1. Examine the method arrayStatistics(self,theArray) what is it returning?
    The min, max, and mean of whatever array is input. This could be just a row or column

'''
 
        