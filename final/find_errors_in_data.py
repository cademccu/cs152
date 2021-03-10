# this script is to find anomalies in the
# csv file, see if its messing up the code
# !!! THIS IS NOT PART OF THE ACTUAL CODE
# !!! I JUST WROTE THIS TO HELP TEST EDGE 
# !!! CASES
def getnum(s):
    return int(s[:-3])

with open("a", "r") as f:
    f.readline() # burn line
    prev = f.readline()
    line =  f.readline() 
    print("-----------------------------------\n")
    while True:
        if not line:
            break
        prev_num = getnum(prev.split(",")[1])
        curr_num = getnum(line.split(",")[1])
        if prev_num == 23:
            if curr_num != 0:
                print("ERROR:", line)
        else:
            if prev_num != (curr_num - 1):
                print("ERROR:", line)
        prev = line
        line = f.readline()
        
    print("-----------------------------------\n")
