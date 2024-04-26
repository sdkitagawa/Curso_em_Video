'''
A teacher wants to draw lots for one of his four students to erase the blackboard. Develop a program to help him by reading their names and typing in the name of the chosen one.

'''

from random import choice

studentList = [ "Jade", "Marlon", "Matthew", "Ismael" ]

print(f"The student chosen is: {choice(studentList)}")
