'''
Develop a program that reads the length of three lines and tells the user whether or not they can form a triangle

'''

firstLine = int(input("\nWelcome to the CiV Labs!\n\nThis is the Triangle Builder!\n\nEnter a value for the first line of your triangle: "))
secondLine = int(input("\nEnter a value for the second line of your triangle: "))
thirdLine = int(input("\nEnter a value for the third line of your triangle: "))
firstLineCheck = firstLine + secondLine

if firstLine < secondLine + thirdLine and secondLine < firstLine + thirdLine and thirdLine < firstLine + secondLine:
    print(f"\nIt is possible to form a triangle with the values ({firstLine}, {secondLine}) and {thirdLine}.")
else:
    print(f"\nIt is not possible to form a triangle with the values ({firstLine}, {secondLine} and {thirdLine}).")
