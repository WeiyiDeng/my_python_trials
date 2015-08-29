# read all info into mylist and use it to get overlap bands for each member
# (with their friends)
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
f = open('/Python34/member_overlap_bands.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(g)
    line = next(r)
    m_id = line[0]
    f_id = line[1]
    member = mylist[int(m_id)]
    friend = mylist[int(f_id)]
    overlap_memberbands = []
    for i in member:
        if i in friend:
            if i not in overlap_memberbands:
                overlap_memberbands.append(i)
    for row in r:
        line = row
        old_mid = m_id
        m_id = line[0]
        f_id = line[1]
        member = mylist[int(m_id)]
        friend = mylist[int(f_id)]
        if m_id != old_mid:
            mydoc.writerow([old_mid,overlap_memberbands])
            overlap_memberbands = []
            for i in member:
                if i in friend:
                    if i not in overlap_memberbands:
                        overlap_memberbands.append(i)            
        else:
            for i in member:
                if i in friend:
                    if i not in overlap_memberbands:
                        overlap_memberbands.append(i)                        
    mydoc.writerow([old_mid,overlap_memberbands])
    d.close()
finally:
    g.close()
    f.close()


###-----------------------------------------------
import csv
import ast

d = open('/Python34/member_overlap_bands.csv','r',encoding="utf-8")
f = open('/Python34/num_overlap_adopt.csv', "w")
mydoc = csv.writer(f, lineterminator='\n')
try:
    r = csv.reader(d)
    numband_adopt = []
    for row in r:
        line = row
        line_mod = ast.literal_eval(line[1])
        numband_adopt.append(len(line_mod))
        mydoc.writerow([line[0],len(line_mod)])
finally:
    d.close()
    f.close()
