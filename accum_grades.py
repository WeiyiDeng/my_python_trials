def read_grades(grade_list):
    ''' (file open for reading) -> dict of {float: list of str}
    Read the grades from grade list into a dictionary where each key is a grade
    and each value is a list of student IDs who earned the grade.

    Precondition: the file grade_list contains a header with no blank lines,
    then a blank line, then lines of student IDs and their grades
    '''

    # skip over the headers
    line = grade_list.readline()
    while line != "\n":
        line = grade_list.readline()

    # read the grades, accumulating them into a dictionary
    line = grade_list.readline()
    dict_grades = {}
    while line != '':
        student_ID = line[:4]
        grade = float(line[4:].strip())
        if grade not in dict_grades:
            dict_grades[grade] =  [student_ID]
        else:
            dict_grades[grade].append(student_ID)        
        line = grade_list.readline()

    return dict_grades
