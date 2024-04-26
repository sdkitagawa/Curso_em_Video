'''
Develop a program that reads any angle and displays the value of the sine, cosine and tangent of that angle on the screen.

'''

from math import sin, cos, tan, radians

angleValue = float(input("Enter the a value for the angle: "))
sineValue = sin(radians(angleValue))
cosineValue = cos(radians(angleValue))
tangentValue = tan(radians(angleValue))

print(f"This is the angle: {(angleValue)}º\nThis is the Sene: {sineValue:.2f}\nThis is the Cosine: {cosineValue:.2f}\nThis is the Tangent: {tangentValue:.2f}")
