# Code a program that reads a value in meters and displays it converted into centimeters and millimeters

meterValue = float(input("Type a value in meters: "))
toCentimeters = meterValue * 100
toMillimeters = meterValue * 1000

print(f"Value in meters: {meterValue} m\nValue in Centimeters: {toCentimeters} cm\nValue in Millimeters: {toMillimeters} ml")
