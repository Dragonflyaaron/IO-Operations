# Read everything in file DOB.
file = open('DOB.txt','r')

names = [] # create a list to store all the names read from the DOB text file
dates = [] # create a list to store all the dates read from the DOB file
n = 1 # counter for the names
d = 1 # counter for the dates
for line in file:
    line = line.strip() # strip any whitespace
    line = line.split() # split the line into pieces
    # each line is split into 5 - the first two become the first and surname, while the other 3 form the dates
    names.append(line[0] + " " + line[1]) # the first two pieces get placed in the name list
    dates.append(line[2] + " " + line[3] + " " + line[4]) # the last 3 get placed in the dates list

print("Names: ")
for i in names: # each name gets printed in the list on a new line
    print ("\t" + str(n) + ".  " +i)
    n +=1

print ("\nBirth Date:")
for j in dates:
    print("\t" + str(d) + ".  " + j)
    d += 1

file.close() # always closing a file to release the resources

