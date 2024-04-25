'''
Write a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m²

Area = Width x Height
Area / 2m²

'''

widthInfo = float(input("Insert the width: "))
heightInfo = float(input("Now type the height: "))
generalArea = widthInfo * heightInfo
paintLiters = generalArea / 2

print(f"The area is: {generalArea} and you going to need {paintLiters} liters of paint.")
