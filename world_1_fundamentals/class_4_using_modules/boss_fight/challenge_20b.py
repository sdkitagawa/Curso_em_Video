'''
The same teacher as in the previous challenge wants to draw lots for the order in which the students will perform. Develop a program that reads the names of the four students and shows the order drawn.

'''

from random import shuffle

firstStudent = str(input("Please enter the name of the first student: "))
secondStudent = str(input("Please enter the name of the second student: "))
thirdStudent = str(input("Please enter the name of the third student: "))
fourthStudent = str(input("Please enter the name of the fourth student: "))

studentList = [ firstStudent, secondStudent, thirdStudent, fourthStudent ]

print(f"The presentation order is: {shuffle(studentList)}")
