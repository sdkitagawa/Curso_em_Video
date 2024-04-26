'''
Develop a program that reads any float number from the keyboard and displays its integer portion.

'''

from math import trunc

floatNumber = float(input("Enter a float number: "))
print(f"This is the integer portion of the entered number: {trunc(floatNumber)}")
