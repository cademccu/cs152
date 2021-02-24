# Your program should count the number of word occurrences contained in a file and 
# output a table showing the top 20 frequently used words in decreasing order of use.

def extract_words(string):
    """
    Returns a list containing each word in the string, ignoring punctuation, numbers, etc.
    DO NOT CHANGE THIS CODE
    """
    l = []
    word = ''
    for c in string+' ':
        if c.isalpha():
            word += c
        else:
            if word != '':
                l.append(word.lower())
            word = ''
    return l
  
def count_words(filename):
    """Returns a dictionary containing the number of occurrences of each word in the file."""
    # create a dictionary
    my_dict = {}
    with open(filename, 'r') as f:
        text = f.read()
        _words = text.split()
        # remove not alpha num bs
        # not gonna use anything fancy 
        words = []
        for s in _words:
            w = ""
            for char in s:
                if char.isalpha():
                    w += char
            words.append(w.lower())
            
        for word in words:
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1

    # open the file and read the text
    # extract each word in the file
    # count the number of times each word occurs.
    # return the dictionary with the word count.
    return my_dict


def report_distribution(count):
    """Creates a string report of the top 20 word occurrences in the dictionary."""
    # create a list containing tuples of count and word,
    # while summing the total number of word occurrences
    num = 0
    tup_list = []

    for key, value in count.items():
        num += int(value)
        tup_list.append((value, key))
    # make me use string formatting smh im gonna use lambas i don't care what we have learned
    #tup_list.sort(key = lambda t: t[0], reverse = True)
    tup_list.sort(reverse = True)

    s_list = []
    s_list.append("{:>5}".format(num))
    max = 10000
    for tup in tup_list:
        if max == 0:
            break
        else:
            max -= 1
        s_list.append("{:>5}".format(tup[0]) + " " + tup[1])

    format_string = "count word\n"
    for i in s_list:
        format_string = format_string + i + "\n"

    # remove last new line im too lazy to do it right in the for-loop
    #format_string = format_string[:-1]
    # add lines with the title and total word count to the output string
    
    # sort the list from largest number to smallest,
    # add a line to the output for each word in the top 20 containing count and word
    
    # return the string containing the report
    return format_string


def main():
    """
    Prints a report with the word count for a file.
    DO NOT CHANGE THIS CODE
    """
    filename = input('filename?\n')
    print(report_distribution(count_words(filename)))


if __name__ == '__main__':
    main()
