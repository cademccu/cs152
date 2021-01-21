# Obtain values for each fill-in-the-blank in the MadLib and place them in a dictionary.
# For 'n' blanks, Split the input sentence into at least n+1 parts. Insert spaces and "\n" wherever needed
#eg. Hello _name_
#   Welcome to _place_.


'''
EXAMPLE
Please excuse Mae
who is far too sleepy
to attend Python class.
'''

# madlib = ["Hello ",
#           "\n",
#           "Welcome to ",
#           "."]

# Define a list of strings containing the MadLib text, including blanks, punctuation, and new lines.
# blanks['name'] = input("name?)
# blanks['place'] = input("place?")

blanks = {}

# fill in blanks
blanks["name"] =  input("name?")
blanks["adjective"] =  input("adjective?")
blanks["noun"] =  input("noun?")

madlib = [ "Please excuse ",
        "\nwho is far too ",
        "\nto attend ",
        " class."]

print(madlib[0] + blanks["name"] + madlib[1] + blanks["adjective"] + madlib[2] + blanks["noun"] + madlib[3])
