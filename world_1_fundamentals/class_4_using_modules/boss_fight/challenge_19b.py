'''
A teacher wants to draw lots for one of his four students to erase the blackboard. Develop a program to help him by reading their names and typing in the name of the chosen one.

Refactoring:
 - User can now set the students names


'''

from random import choice

firstStudent = str(input("Please enter the name of the first student: "))
secondStudent = str(input("Please enter the name of the second student: "))
thirdStudent = str(input("Please enter the name of the third student: "))
fourthStudent = str(input("Please enter the name of the fourth student: "))

studentList = [ firstStudent, secondStudent, thirdStudent, fourthStudent ]

print(f"The student chosen is: {choice(studentList)}")
