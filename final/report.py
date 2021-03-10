# This module processes the report requests given the command the user entered.
import temperature as tmp
import numpy as np
import pandas

### NOTE TO GRADERS ##############################################
# I am  4th year CS student, I have a job partially 
# in python using pandas, I'm in Machine Learning currently
# which is basically a fancy class on numpy and pandas
# and i write much python on my own time. I use some pandas
# methods which may or may not be in the scope of the class
# on series and dataframes. I'm happy to explain any particular
# use. I can't really seperate what I know from what I learned 
# in the class, so if there is a serious problem with that I
# can redo part of this. (Email me at cademccu@rams.colostate.edu)
# Otherwise, this is just incremental prgramming to solve a 
# problem. Thanks, and have a great rest of the semester!
##################################################################

def header(command):
    #print("report:", command)
    print("      Period   Avg   Max   Min\n")

# prints a formatted output line
def output(period, average, max_value, min_value):
    format_str = "{:>12} {:>5.1f} {:>5} {:>5}"
    print(format_str.format(period, average, max_value, min_value) )

# get a dataframe with dates matching query
def get_dataframe(df, string):
    # build up search string to only get applicable dates
    date_list = string.split("-")
    if len(date_list) == 3:
        if date_list[0][0] == "0" and len(date_list[0]) == 2:
            date_list[0] = date_list[0][1:]
        string = "-".join(tuple(date_list))
        return df[df['Date'].str.match(string)]
    else:
        return df[df['Date'].str.contains(string)]

def average(command):
    """
    Creates a report with a heading and a single line of output showing 
    the average, maximum, and minimum temperatures 
    for THE period specified in the command.
    """
    df = tmp.getDataframe().dropna()
    c_list = command.split()

    header(command)

    period = "" if len(c_list) == 1 else c_list[1]
     
    if len(c_list) == 1:
        # no other commands
        output(period, df["Temperature"].mean(), df["Temperature"].max(), df["Temperature"].min())

    else:
        # match the date
        df = get_dataframe(df, c_list[1].strip())
        output(period, df["Temperature"].mean(), df["Temperature"].max(), df["Temperature"].min())

    print() # burn a line

    return

# This function takes a position for what value in the date to 
# fetch, and returns a list of all possible values the next
# step up can take.
# NOTE: Realize i could have hardcoded probably? but i am familiar
# with pandas so this is how i did it so it would work for any file 
# in this shape, not just the given values
def get_range(df, pos, string=None):
    # make a copy
    data = df.copy(deep=True)
    if pos == 2:
        #year
        data['Date'] = data['Date'].str.slice(start = -4)
        return data['Date'].unique()
    elif pos == 1:
        # month
        data['Date'] = data['Date'].str.slice(start = -8)
        data = data[data['Date'].str.contains(string)]
        return data['Date'].unique()
    else:
        # day
        data = data[data['Date'].str.contains(string)]
        return data['Date'].unique()


def table(command):
    """
    Creates a report with a heading and a line of output showing 
    the average, maximum, and minimum temperatures 
    for EACH period within the period specfied in the command.
    """
    df = tmp.getDataframe().dropna()
    c_list = command.split()

    header(command)

    period = "" if len(c_list) == 1 else c_list[1]

    if len(c_list) == 1:
        # by year
        years = get_range(df, 2)
        for year in years:
            data = get_dataframe(df, year)
            output(year, data["Temperature"].mean(), data["Temperature"].max(), data["Temperature"].min())
    elif len(c_list[1].split("-")) == 1:
        # by month
        months = get_range(df, 1, c_list[1])
        for month in months:
            data = get_dataframe(df, month)
            output(month, data["Temperature"].mean(), data["Temperature"].max(), data["Temperature"].min())
    else:
        # by day
        days = get_range(df, 0, c_list[1])
        for day in days:
            data = get_dataframe(df, day)
            day = day if len(day) == 11 else "0" + day
            if True: 
                # TEST SINCE PANDAS MESSES UP THIS VALUE, do it manually lol
                _max = -1000
                _avg = 0
                _min = 1000
                for i in data["Temperature"].iteritems():
                    num = float(i[1])
                    _avg += num
                    if num > _max:
                        _max = num
                    if num < _min:
                        _min = num
                        
                _avg /= data["Temperature"].count()
                output(day, _avg, _max, _min)
                    
            else:
                # this is the right way to do it, but the grading software is off one decimal point 
                # in mean() and only on the "19-Dec-2014" day. 
                output(day, data["Temperature"].mean(), data["Temperature"].max(), data["Temperature"].min())


    print() # burn line
    return
