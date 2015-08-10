# tuples
A = [1,2,3]
A[0]
A[0] = 0
A
### lists are mutable, can assign item directly

tup = ("a", 2, 3.0)
tup[0]
tup[-1]
# tup[1] = 5    will return an error
### tuples are immutable, cannot assign new value to item

dir(list)
dir(tuple)

for i in tup:
    print(i)
    
for i in range(len(tup)):
    print(tup[i])
    
(1,2)
(1,)                 # create a tuple with single item
# (1) will just return 1, not a tuple 
()                   # create an empty tuple



#
# dictionaries
A = {'a1':70, 'a2': 80, 'a3':90}      # creates a dictionary {key:value}
A['a2']                      # returns value 80
# keys need to be unique

'a1' in A       # check for keys in the dictionary, not values
'a4' in A
80 in A         # returns false

len(A)

### dictionaries are mutable, can add or change key-value pairs
A['a4'] = 85    
A
len(A)
A['a3'] = 100

del A['a4']             # delete from the dictionary using keys
len(A)
A

for i in A:
    print(i)            # will print the keys 
    
for i in A:
    print(A[i])         # print the values 

for i in A:
    print(i, A[i])      # print both
    
d = {}                  # create an empty dictionary
len(d)

d = {'a':45, 8: 'banana'}        # keys and values can be of different types
d[8]
d[9] = 100                       # add another key 9 with value 100

### keys must be immutable, using list as key will give an error 
# d[[1,2]] = 'car' gives an error  
d[(1,2)] = 'car'                 # can use tuples as keys
d



# accumulate values with replicated keys with lists
fruit_to_color = {
    "banana": "yellow",
    "cherry": "red",
    "orange": "orange",
    "pear": "green",
    "peach": "orange",
    "watermelon": "red",
    "stawberry": "red"}

color_to_fruit = {}
for i in fruit_to_color:
    color = fruit_to_color[i]
    color_to_fruit[color] = i   # missing some fruits because of replicated keys

color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    if color not in color_to_fruit:
        color_to_fruit[color] = [fruit]    # make fruit into a list of str ! otherwise cannot append later
    else:
        color_to_fruit[color].append(fruit)



#
import accum_grades
grade_route = "/Python34/a1_test.txt"
grade_list = open(grade_route, 'r')

dict_grades = accum_grades.read_grades(grade_list)

grade_list.close()



