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

f = open('/Python34/count_user_bands.csv', "w")  # creates a file automatically
# mywrite = csv.writer(trywrite, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
mydoc = csv.writer(f, lineterminator='\n')
# Need to put in (lineterminator='\n') in csv.writer
# Otherwise writes a space line between each observation
##for i in mydict:
##    mydoc.writerow([i,mydict[i]])

for i in range(len(user_ID)):
    mydoc.writerow([user_ID[i],sum_weeks[i]])

f.close()
