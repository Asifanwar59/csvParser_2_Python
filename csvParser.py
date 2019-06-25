#!/usr/bin/env python
"""
The task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. Extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
csv module's "reader" method is used to get data in such format.
Another useful method is next() - to get the next line from the iterator.

"""

import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        fileText = csv.reader(f)

        index = 0
        for lineNum, lineContent  in enumerate(fileText):
            try:
                if index == 0:
                    name = lineContent[1]
                    index = 1
                elif index == 1:
                    index = 2
                else:
                    data.append(lineContent)  

            except StopIteration:
                pass
        pass
    print("Length of the list:",len(data))
    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
