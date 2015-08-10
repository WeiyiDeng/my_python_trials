if 8 > 5:
    print('bite me')

sports = False
bike = 20
if sports == True:
    if bike > 30:
        print("Run instead")
    else:
        print("buy a bike")
else:
    print("sit watch TV")


"us" in "lousy"

len("haha"*3 + "btw")

"" in "cat"

A = 'learn'
A[0]
A[1:3]
len(A)
A[3:len(A)]
A[1:-2]
A[0:5]
A[:]
A[:3]
A[3:]

A = "learn to do"
A[:5]+'ed'+A[5:]
A = A[:5]+'ed'+A[5:]
A = A[:3]+A[4]+ ' on'

# string methods
myquote = 'let\'s get this over with'
dir(myquote)
help(myquote.count)          # same as
help(str.count)

myquote.capitalize()
myquote.upper()
myquote.lower()

myquote.count("lets")        # count number of times the sub str appear in str
myquote.count("let")
myquote.count("e")

myquote.find('th')           # find starting index of the sub str
myquote.rfind('th')          # find index from the right
myquote.find('get',3)        # starting from index 3 of the original str
myquote.find('get',8)        # produces -1 if not found

a = '	No idea what to do '
a.lstrip()
a.rstrip()
a.strip()

my = 'I bought an ipod in the store'
my.count("i")
my.lower().count("i")       # can use two methods sequentially

# for loop
a = "what to eat"

for i in a:
    print(i*2)









