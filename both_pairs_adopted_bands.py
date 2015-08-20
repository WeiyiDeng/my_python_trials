### trial process
##import csv
##f = open('/Python34/wtry1.csv', "w")
##mydoc = csv.writer(f, lineterminator='\n')
##A = [{1:42,2:4},{'qeq':3,'fwf':4},{5:65,6:90},7]
##for i in A:
##    mydoc.writerow([i])
##f.close()
##d = open('/Python34/wtry1.csv','r',encoding="utf-8")
##r = csv.reader(d)
##header = next(r)
##header                            # header is a str with dict structure inside
##import ast
##ast.literal_eval(header)          # convert the str back to dict
##B = ast.literal_eval(header)
##B[1]
##d.close()

import csv

# read lines one by one
# saving aggregrated info of all individuals in memory
d = open('/Python34/bandadoptions3.csv','r',encoding="utf-8")
f = open('/Python34/adoptiondict.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(d)
    line_old = next(r)              # read first line
    mylist = [{int(line_old[1]):int(line_old[2])}]
    ind = 0
    for row in r:
        line_new = row
        if line_new[0] == line_old[0]:
            mylist[ind][int(line_new[1])] = int(line_new[2])
        else:
            mylist.append({int(line_new[1]):int(line_new[2])})
            mydoc.writerow([mylist[ind]])
            ind = ind+1
        line_old = line_new
        mydoc.writerow([line_old[0],mylist[ind]])
finally:
    d.close()
    f.close()


# not saving aggregrated info of all individuals in memory
# write a row as soon as finish reading all lines(one by one) of a person
d = open('/Python34/bandadoptions3.csv','r',encoding="utf-8")
f = open('/Python34/adoptiondict.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(d)
    line_old = next(r)              # read first line
    mydict = {int(line_old[1]):int(line_old[2])}
    for row in r:
        line_new = row
        if line_new[0] == line_old[0]:
            mydict[int(line_new[1])] = int(line_new[2])
        else:
            mydoc.writerow([line_old[0],mydict])
            mydict = {int(line_new[1]):int(line_new[2])}
        line_old = line_new
    mydoc.writerow([line_old[0],mydict])           # last individual
finally:
    d.close()
    f.close()

### -------------------- testing -------------------------------
import ast
ast.literal_eval(header)         # convert str to dict

import linecache                 # get specific line without reading whole file
line = linecache.getline('/Python34/adoptiondict.csv',2)

# read each line at a time
# have to start all over again to find next index
d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
r = csv.reader(d)
ww = next(r)
while ww[0] != '2':
    ww = next(r)

# or alternatively
# have to start all over again to find next index
d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
r = csv.reader(d)
myselect = [row for row in r if row[0] == '2']

# or read the whole file into memory as a large list
# still need to re-start to find another line
d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
r = csv.reader(d)
list(r)[1]

# based on line number
# will NOT start again
f = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
for i, line in enumerate(f):
    if i == 2:
        print(line)
    elif i == 2:
        print(line)
    elif i > 3:
        break


###----------------------------------------------------------------
# have to re-start each time to read specific lines
# very slow

import csv
import ast

g = open('/Python34/friends3.csv','r',encoding="utf-8")
f = open('/Python34/adoptionpairs.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(g)    
    both_adopt_list = []
    week_diff_list = []
    for row in r:
        line = row
        m_id = line[0]
        f_id = line[1]
        d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
        k = csv.reader(d)
        member = [myrow for myrow in k if myrow[0] == str(m_id)]
        d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
        k = csv.reader(d)
        friend = [myrow for myrow in k if myrow[0] == str(f_id)]
        member = member[0]                # unlist
        friend = friend[0]
        member = ast.literal_eval(member[1])       # convert str to dict
        friend = ast.literal_eval(friend[1])
        both_adopt = 0
        week_diff = []
        for i in member:
            if i in friend:
                if member[i] < friend[i]:
                    both_adopt = both_adopt + 1
                    week_diff.append(friend[i] - member[i])
        mydoc.writerow([both_adopt,week_diff])
        both_adopt_list.append(both_adopt)
        week_diff_list.append(week_diff)
        d.close()
finally:
    g.close()
    f.close()

###--------------------------------------------------------------
import csv
d = open('/Python34/bandadoptions3.csv','r',encoding="utf-8")
f = open('/Python34/wtryverify.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    mylist = ['header']
    r = csv.reader(d)
    line_old = next(r)              # read first line
    mylist.append({int(line_old[1]):int(line_old[2])})
    ind = 1
    for row in r:
        line_new = row
        if line_new[0] == line_old[0]:
            mylist[ind][int(line_new[1])] = int(line_new[2])
        else:
            mylist.append({int(line_new[1]):int(line_new[2])})
            mydoc.writerow([line_old[0],mylist[ind]])
            ind = ind+1
        line_old = line_new
    mydoc.writerow([line_old[0],mylist[ind]])
finally:
    d.close()
    f.close()

g = open('/Python34/friends3.csv','r',encoding="utf-8")
f = open('/Python34/adoptionpairs.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(g)    
    both_adopt_list = []
    week_diff_list = []
    for row in r:
        line = row
        m_id = line[0]
        f_id = line[1]
        member = mylist[int(m_id)]
        friend = mylist[int(f_id)]
        both_adopt = 0
        week_diff = []
        # week_f = []
        # week_m = []
        for i in member:
            if i in friend:
                both_adopt = both_adopt + 1
                # week_f.append(friend[i])
                # week_m.append(member[i])
                week_diff.append((friend[i] - member[i]))
        # mydoc.writerow([both_adopt,week_f,week_m,week_diff])
        mydoc.writerow([both_adopt,week_diff])
        both_adopt_list.append(both_adopt)
        week_diff_list.append(week_diff)
        d.close()
finally:
    g.close()
    f.close()


###--------------------------------------------------------------
import csv
import ast

d = open('/Python34/adoptiondict.csv','r',encoding="utf-8")
f = open('/Python34/num_bandadopt.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(d)
    numband_adopt = []
    for row in r:
        line = row
        line = ast.literal_eval(line[1])
        numband_adopt.append(len(line))
        mydoc.writerow([len(line)])
finally:
    d.close()
    f.close()


###---------------------------------------------------------------
d = open('/Python34/adoptionpairs.csv','r',encoding="utf-8")
f = open('/Python34/adoptionpairs_mod.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(d)
    for row in r:
        line = row
        line = ast.literal_eval(line[1])
        for j in line:
            mydoc.writerow([j])
finally:
    d.close()
    f.close()













