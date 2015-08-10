i = 1
while i < 100:
    i = i * 5
    print(i)

i = 0
s = "dwy"
while i < len(s) and s[i] not in "aeiouAEIOU":
    print(s[i])
    i = i + 1

#
ww = [0]*5                     # returns a list of 5 zero items
ww
grades = [70, 80, 90]          # grades is list variable
dir(grades)
help(grades.append)
grades.append(100)

max(grades)
min(grades)
len(grades)
sum(grades)

import statistics            # need to import module to calculate mean of a list
statistics.mean(grades)

90 in grades
60 in grades

grades[0]
grades[3]

# slice index returns a list rather than an element
grades[3:]            # returns [100] 
grades[-1]            # returns 100
grades[3:] == grades[-1]       # returns false, list is not the same as elements
# E: [25] != 25 returns true

grades.append("NA")         # can add different types of elements in same list

grades.extend([800,700])

subjects = ["chem", "bio", "math", "cs"]

subjects[2]
dir(subjects)
len(subjects)
max(subjects)
min(subjects)
subjects.append(6)

address = ["Baker Street", 30]

for i in grades:
    print(i)


s = ""
names = ["Alice", "Bob", "Carol"]
for name in names:
    s = s + name
# s will refer to "AliceBobCarol"



colors = []
prompt = 'Enter one of your favourite colors, press enter to end'
inputcolor = input(prompt)
while inputcolor != '':
    colors.append(inputcolor)         # notice here cannot use colors = colors.append(inputcolor) ! returns None
    inputcolor = input(prompt)
    
colors.extend(["black", "pink"])      # input is a list

colors.pop()                  # removes last item from the list and returns it
colors.pop(2)                 # removes the item at index 2

if "yellow" in colors:
	colors.remove("yellow")

colors.extend(["aqua green", "classic red"])
colors.sort()
colors.reverse()
colors.insert(-2,"orange")
colors.index("orange")

if "pink" in colors:
    where = colors.index("pink")
    colors.pop(where)
    

# Alias and mutabilty of list object
list1 = [0, 2, 4, 6, 8]
list2 = list1                  # two variables refer to the same list (aliasing)
list1[-1] = 11
print(list1)
print(list2)                   # when list1 changes the list, list2 also changes

def double_even_indices(lst):
    """ (list of int) -> None
    Double every other int in lst.
    """
    i = 0
    while i < len(lst):
        lst[i] = lst[i]*2
        i = i+2

list1 = [11,12, 13, 14, 15, 16, 17]
print(list1)
double_even_indices(list1)      # within the function the list obj is changed
print(list1)                    # variable list1 also changed because it refers to the list object

# only list object is mutable (will be change in function or by alias)
# be careful when writing functions !!

# use range for indexing
mystr = "what a day"
for i in mystr:
    print(i)

mylist = [1,2,3]
for i in mylist:
    print(i)

help(range)                 # range can let index starts from random location     
for i in range(len(mystr)):
    print(i)
    print(mystr[i])

for i in range(1,len(mystr),3):       
    print(mystr[i])

# lists within lists
grades = [["stat",80],["math",90],["cs",100]]
len(grades)
grades[0]
len(grades[1])
grades[2][1]

for i in grades:
    print(i)

for i in range(7,10):
    for j in range(1,4):
            print(i,j)


# read file into python
trycsv = "/Python34/imat1578.csv"
mytextfile = open(trycsv, 'r')          # w for write and erase and a for append
mytextfile.readline()
mytextfile.close()                      # to close the file

pretentious = "/Python34/Hemingway.txt"
mytext = open(pretentious, 'r')
mytext.readline()
mytext.close()

mytext = open(pretentious, 'r')       # read each line at a time automatically
line = mytext.readline()
while line != '':
    print(line)
    line = mytext.readline()
mytext.close()

print("we are \n the world\n")      # print will start new line if there is \n

mytext = open(pretentious, 'r')
line = mytext.readline()
while line != '':
    print(line, end = '')           # to get rid of space lines
    line = mytext.readline()
mytext.close()


mytext = open(pretentious, 'r')       # read only the first paragraph
line = mytext.readline()
while line != '\n':
    print(line, end = '')       
    line = mytext.readline()
mytext.close()


mytext = open(pretentious, 'r')       # use simple for loop to read whole file
for i in mytext:
    print(i, end = '')    
mytext.close()

mytext = open(pretentious, 'r')
# mytext.read()                         # read whole file as a str at once
wholetxt = mytext.read()            
print(wholetxt)
mytext.close()

mytext = open(pretentious, 'r')
# mytext.readlines()               # read lines can also read all txt at once
lines = mytext.readlines()       # lines are stored as list items by readlines
for i in lines:
    print(i, end = '')
mytext.close()
lines[0]
lines[1]

# use module to create new file
import tkinter.filedialog
tkinter.filedialog.askopenfilename()   # open file in python to get file address
from_filename = tkinter.filedialog.askopenfilename()
to_filename = tkinter.filedialog.asksaveasfilename() # select place to save file

mytext = open(from_filename, 'r')       # copy from original file
content = mytext.read()
mytext.close()
content

mycopytext = open(to_filename, 'w')     # write into new file
mycopytext.write("copy\n author: DXM\n")   # add some more content
mycopytext.write(content)
mycopytext.close()


# convert a list to str
list1 = ['1', '2', '3']
str1 = ''.join(list1)

##------------------- using csv module to read data -----------------------
# 
import csv
d = open("imat1578.csv",'r')
r = csv.reader(d)
line = next(r)
sum_DV = 0
while line != '':
    sum_DV = sum_DV + int(line[3])
    line = next(r)    
d.close()

# or alternatively
d = open("imat1578.csv",'r')
r = csv.reader(d)
sum_DV = 0
for row in r:
    line = row
    sum_DV = sum_DV + int(line[3])
    
d.close()


# can also open tsv file with the csv module
f = open('/Python34/aggregate.artist.tsv','r')
z = csv.reader(f, delimiter='\t')
line1=next(z)

f.close()

# same as
with open('/Python34/aggregate.artist.tsv','r') as f:
    z = csv.reader(f, delimiter='\t')
    line1=next(z)
    line1=next(z)
# here file closes automatically after executing with

# same as below

##------------- find out how many weeks each user appears in ------------
# w: beware of the codings !!
import csv
d = open('/Python34/aggregate.artist.tsv','r',encoding="utf-8")
try:
    r = csv.reader(d, delimiter='\t')
    header = next(r)               # skip header
    mydict = {}
    for row in r:
        line = row
        if line[0] not in mydict:
            mydict[line[0]] = [line[3]]
        else:
            if line[3] not in mydict[line[0]]:
                mydict[line[0]].append(line[3])        
finally:
    d.close()

mydict['AbsMusic']

# sum up total weeks num for each user
sum_weeks = []
user_ID = []
for i in mydict:
    print(i,len(mydict[i]))
    user_ID.append(i)
    sum_weeks.append(len(mydict[i]))

f = open('/Python34/trialwrite.csv', "w")  # creates a file automatically
# mywrite = csv.writer(trywrite, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
mydoc = csv.writer(f, lineterminator='\n')
# Need to put in (lineterminator='\n') in csv.writer
# Otherwise writes a space line between each observation
##for i in mydict:
##    mydoc.writerow([i,mydict[i]])

for i in range(len(user_ID)):
    mydoc.writerow([user_ID[i],sum_weeks[i]])

f.close()

#------------------------------------------------------------
# try this!
for i in mydict.keys():
    print(i)                 # will print all the keys

# split in str to create list of items based on space
help(str.split)
A = 'what the hell'
A.split()


 


