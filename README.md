# csvParser_2_Python
Process the supplied csv file and use the python's csv module to extract data from it.

# Introduction:
The task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. Extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
csv module's "reader" method is used to get data in such format.
Another useful method taht cvan be used is next() - to get the next line from the iterator.

# Input file:
745090.csv
