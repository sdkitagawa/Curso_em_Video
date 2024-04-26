'''
Develop a program that reads the length of the opposite and adjacent sides of a right triangle, calculates and displays the length of the hypotenuse

'''

from math import hypot

oppositeSide = float(input("Enter the value for the Opposite side: "))
adjacentSide = float(input("Enter the value for the Adjacent side: "))
lengthHypotenuse = hypot(oppositeSide, adjacentSide)

print(f"The lenght of the hypotenuse is: {lengthHypotenuse:.2f}")
