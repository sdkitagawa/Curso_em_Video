'''
The same teacher as in the previous challenge wants to draw lots for the order in which the students will perform. Develop a program that reads the names of the four students and shows the order drawn.

'''

from random import shuffle

studentList = [ "Jade", "Marlon", "Matthew", "Ismael" ]
shuffle(studentList)

print(f"The presentation order is: {studentList}")
