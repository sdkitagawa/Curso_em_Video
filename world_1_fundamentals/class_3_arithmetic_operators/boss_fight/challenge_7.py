'''
Develop a program that reads a student's two grades, calculates and displays their average

G1: Grade 1
G2: Grade 2
GG: The amount o grades you have in general

Average = G1 + G2 / GG

E.g: Average = 10 + 10 + 6 / 3
'''

8
firstGrade = float(input("Insert the first grade: "))
secondGrade = float(input("Insert the second grade: "))

averageGrade = (firstGrade + secondGrade) / 2

print(f"The average grade is: {averageGrade}")
