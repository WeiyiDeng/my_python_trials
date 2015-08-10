import math
import randomfunction            # import name of the module file !

def trialsquaring(value1, value2):
    """
    Pre-condition: value1 > 0 and value2 > 0
    """
    return math.sqrt(randomfunction.halfpower(value1, value2))

def tryif(x,y):
    if x > y:
        return 'big'
    elif x < y:
        return 'small'
    else:
        return 'equal'

##def tryif2(x,y):
##    if x > y:
##        return True
##    return False
##
##def tryif3(x,y):                # these two are equivalant
##    return x > y

def count_vowels(mystr):
    """ (str) -> int

    Returns the number of vowels in mystr.

    <<< count_vowels('when will the wifi work')
    6
    <<< count_vowels('uber')
    2
    """
    count_num = 0
    for i in mystr:
        if i in "aeiouAEIOU":
            count_num = count_num + 1
    return count_num



def collect_vowels(mystr):
    """ (str) -> str
    Collects the vowels in mystr
    <<< collect_vowels('uber')
    "ue"
    """
    collect_str = ""
    for i in mystr:
        if i in "aeiouAEIOU":
            collect_str = collect_str + i
    return collect_str

collect_vowels('merry chrismas')


def up_to_vowels(mystr):
    """ (str) -> str
    >>> up_to_vowels("there")
    "th"
    >>> up_to_vowels("cs")
    "cs"
    """
    gather_vowels = ''
    i = 0
    while i < len(mystr) and mystr[i] not in "aeiouAEIOU":
        print(mystr[i])
        gather_vowels = gather_vowels + mystr[i]
        i = i + 1
    return gather_vowels

checkout = up_to_vowels("cs")


def get_answer(prompt):
    """ (str) -> str
    """
    answer = input(prompt)
    while not (answer.lower() == "yes" or answer.lower() == "no"):
        answer = input(prompt)
    return answer

# E: get_answer("Are you hungry?")


    
def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s)-1
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]                  # return ends the function
        i = i - 1
    return None


def count_adjacent_repeats(mystr):
    """ (str) -> int
    Returns the number of occurences of a charater and the one next to
    it being the same.
    >>> count_adjacent_repeats('abbseetffg')
    3
    """
    repeats = 0
##    for i in range(1,len(mystr)):
##        if mystr[i] == mystr[i-1]:
    for i in range(len(mystr)-1):               # same as above
        if mystr[i] == mystr[i+1]:
            repeats = repeats + 1
    return repeats
        

def shift_left(mylist):       # the function is for changing the list, no return
    """ (list) -> Nonetype
    Shift each item in the list to the left and the first element to
    the last.

    Pre-condition: len(mylist) >= 1
    """
    first_ele = mylist[0]

    for i in range(1,len(mylist)):
        mylist[i-1] = mylist[i]

    mylist[-1] = first_ele

somelist = ['a','b','c','d']
print(shift_left(somelist))            # returns None
print(somelist)


    
def sum_items(list1,list2):
    """ (list of number, list of number) -> list of number
    Returns a new list of the summed values of corresponding
    elements of list1 and list2.

    Pre-condition: len(list1) == len(list2)

    >>> sum_items([1,2,3],[4,5,6])
    [5,7,9]
    """

    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list
    

# can use this function to find matches for strings or lists
def count_matches(str1, str2): 
    """ (str, str) -> int
    Return the number of positions in str1 that contain the same character at the
    corresponding position of str2.
    Precondition: len(str1) == len(str2) """
    num_matches = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            num_matches = num_matches + 1
    return num_matches

count_matches("abe", "ape")
count_matches([1,2,3], [2,2,5])


#
def calculate_avg(assign_grades):
    """ (list of list of [str, number]) -> float

    Returns the average of grades in assign_grades.

    >>> calculate_avg([['ass1',80],['ass2',90]])
    85.0
    """
    total = 0
    for i in assign_grades:                # i is list0, list1, list2, list3...
        total = total + i[1]

    return total/len(assign_grades)

calculate_avg([['ass1',80],['ass2',90]])


def avg_gradelist(grade_list):
    """ (list of list of numbers) -> list of float
    >>> avg_gradelist([[85,80,90],[70, 80 ,90, 100],[80,100]])
    [85.0,85.0,90.0]
    """
    averages = []
    for i in range(len(grade_list)):         # i is 0, 1, 2, ... here
        averages.append(sum(grade_list[i])/len(grade_list[i]))
    return averages
        
# same as above    
def avg_gradelist2(grade_list):
    """ (list of list of numbers) -> list of float
    >>> avg_gradelist2([[85,80,90],[70, 80 ,90, 100],[80,100]])
    [85.0,85.0,90.0]
    """
    averages = []
    for i in grade_list:         # i is list0, list1, list2, ... here
        total = 0
        for j in i:
            total = total + j
        averages.append(total/len(i))
    return averages













    
