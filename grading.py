def gradingStudents(grades):
    # Write your code here
    lst = []
    for grade in grades:
        if grade >= 38:
            if grade % 5 == 3:
                grade += 2
            elif grade % 5 == 4:
                grade += 1
        lst.append(grade)
    return lst


my_grade = [29, 73, 40, 56]
print(gradingStudents(my_grade))
