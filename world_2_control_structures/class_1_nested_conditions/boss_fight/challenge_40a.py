'''
Develop a program that reads two grades from a student and calculates their average, displaying a message at the end according to the average achieved:

- Average below 5.0: Fail;
- Average between 5.0 and 6.9: Summer Classes;
- Average 7.0 or above: Pass.

'''

first_grade = float(input("\nWelcome to the CiV Labs\n\nThis is the Average Calculator\nPlease enter first grade of your student: "))
second_grade = float(input("\nGood, now enter the second grade: "))
grade_calculator = (first_grade + second_grade) / 2

if grade_calculator < 5:
    print("This student has failed the exam! They are reproved.")
elif grade_calculator <=6.9 and grade_calculator >= 5.0:
    print("This student has failed and will have to attend classes during the summer.")
else:
    print("This student has aced exams! They are approved!")
