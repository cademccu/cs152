# This module processes the input file given its filename.

import pandas
import numpy as np



def readData(filename):
    """
    Gather data from the input file.
    Use a data structure that will help you analyze and report the data.
    """
    global data
    data = pandas.read_csv(filename, na_values="***")
    return


def getDataframe():
    return data

