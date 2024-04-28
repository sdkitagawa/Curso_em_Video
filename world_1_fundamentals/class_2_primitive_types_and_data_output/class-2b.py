'''
Primitive Types are basically the several variable types, e.g: int, float, bool and str

Int ➝ Integer: 7, -4, 0, 9875
Float ➝ Floating Point: 4.5, 0.076, -15.223, 7.0
Bool ➝ Boolean: True, False
Str ➝ String: "Hello", "7.5", ""

You can check if a number is Numeric, Alphabetic, Alpha Numeric, Uppercase, Lowercase, Printable, Space, Decimal or identifier.
'''
testFlight = input("Type something so I can check: ")

# Testing types

print(f"Is it Numeric: {testFlight.isnumeric()}")
print(f"Is it Alphabetic: {testFlight.isalpha()}")
print(f"Is it Alphanumeric: {testFlight.isalnum()}")
print(f"Is it Uppercase: {testFlight.isupper()}")
print(f"Is it Lowercase: {testFlight.islower()}")
print(f"Is it Printable: {testFlight.isprintable()}")
print(f"Is it a space character: {testFlight.isspace()}")
print(f"Is it a decimal character: {testFlight.isdecimal()}")
print(f"Is it an identifier: {testFlight.isidentifier()}")

'''
Old Format:

print("Is it Numeric: {}".format(testFlight.isnumeric()))
print("Is it Alphabetic: {}".format(testFlight.isalpha()))
print("Is it Alphanumeric: {}".format(testFlight.isalnum()))
print("Is it Uppercase: {}".format(testFlight.isupper()))
print("Is it Lowercase: {}".format(testFlight.islower()))
print("Is it Printable: {}".format(testFlight.isprintable()))
print("Is it a space character: {}".format(testFlight.isspace()))
print("Is it a decimal character: {}".format(testFlight.isdecimal()))
print("Is it an identifier: {}".format(testFlight.isidentifier()))
'''
