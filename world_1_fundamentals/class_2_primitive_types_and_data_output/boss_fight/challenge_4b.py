# Develop a program that can read an input and print out its primitive type and possibly information about the data type

checkInput = input("Type something: ")
print(f"The data type is: {type(checkInput)}")
print(f"Is it Numeric: {checkInput.isnumeric()}")
print(f"Is it Alphabetic: {checkInput.isalpha()}")
print(f"Is it Alphanumeric: {checkInput.isalnum()}")
print(f"Is it Uppercase: {checkInput.isupper()}")
print(f"Is it Lowercase: {checkInput.islower()}")
print(f"Is it Printable: {checkInput.isprintable()}")
print(f"Is it a space character: {checkInput.isspace()}")
print(f"Is it a decimal character: {checkInput.isdecimal()}")
print(f"Is it an identifier: {checkInput.isidentifier()}")

'''
Old Format:

print(f"The data type is: {type(checkInput)}")
print("Is it Numeric: {}".format(checkInput.isnumeric()))
print("Is it Alphabetic: {}".format(checkInput.isalpha()))
print("Is it Alphanumeric: {}".format(checkInput.isalnum()))
print("Is it Uppercase: {}".format(checkInput.isupper()))
print("Is it Lowercase: {}".format(checkInput.islower()))
print("Is it Printable: {}".format(checkInput.isprintable()))
print("Is it a space character: {}".format(checkInput.isspace()))
print("Is it a decimal character: {}".format(checkInput.isdecimal()))
print("Is it an identifier: {}".format(checkInput.isidentifier()))
'''
