'''
Manipulating Text Strings

Themes:
 - Slicing
 - Lenght
 - Count
 - Transform ➝ Upper, Lower, Capitalize, Title, Strip
 - Division ➝ Split, Join
 
'''

numberCollection = "0123456789"
basicTextSlicing = "We lost the Data Keys"
stringAnalysis = "this is a string being used for analysis"
userAgeInput = "     40 years old     "
serialNumber = "AXH2K C0SC2 1456A CD94A 16892"

# Looking for the number 9 as a string using the List Data Structure
print(numberCollection[9])

'''
Printing out from the strings inside the variable basicTextSlicing starting from the index 12 and stopping by index 20 to print out from index 12 to 21 which corresponds to "Data Keys"

This a simple representation of how it works.

W e <space character> L o s t <space character> t h  e <space character> D  a  t  a <space character> K  e  y  s  (Endpoint)
0 1        2          3 4 5 6         7         8 9 10        11         12 13 14 15        16        17 18 19 20    21
'''
print(f"Slice of a string from the index 12 to 20: {basicTextSlicing[12:21]}")

# This time printing out from the index 12 up to 19 (from 12 to 20 not including the 20), but skipping two indexes (and showing the second)
print(f"Slice of a string from the index 12 to the index 20, but skipping two indexes (and showing the second one): {basicTextSlicing[12:20:2]}")

# Printing out from the index 0 to the index 4 (from 0 to 5 considering 5 as an endpoint)
print(f"Slice of a string from the index 0 to the index 4: {basicTextSlicing[:5]}")

# We can use this to print something out starting from the index 17 by the last index available
print(f"Slice of a string from the index 17 the last index: {basicTextSlicing[17:]}")

# We can use this to print something out starting from the index 12 by the last index available but skipping three indexes (and showing the third)
print(f"Slice of a string from the index 12 to the last index, but skipping three indexes (and showing the third one): {basicTextSlicing[12::3]}")

# Printing out the default value of our submitted string for Analysis
print(f"This what we have inside of our String being used for Analysis: {stringAnalysis}\n")

# The "len" method it's basically used to check the lenght of anything, from strings, arrays and data-structures
print(f"The lenght of the string \"stringAnalysis\" is: {len(stringAnalysis)}\n")

# The "count" method can be used to count the amount of anything, for example, to count how many times a character is appears in a sentence
print(f"The amount of \"a\"'s inside \"stringAnalysis\" is: {stringAnalysis.count("a")}\n")

# We can also define a start and endpoint index so you can count and slice at the same time
print(f"Starting from the index 0 going to index 10 (but, actually stopping by 9) what is the amount of \"a\"'s inside \"stringAnalysis\" is: {stringAnalysis.count("a", 0, 10)}\n")

# There's a method called "find" that can be use to find a value inside of a String, Dictionary, List, Tuple (Arrays) and etc.
print(f"In which index inside \"stringAnalysis\" can we find \"is\": {stringAnalysis.find("is")}\n")
print(f"When we try to find a word that is not present inside our string we see this value: {stringAnalysis.find("Luma")}\n")

# The "in" operator can be used to check if something is INside another thing.
print(f"Is the word Luma present inside the \"stringAnalysis\" variable: {"Luma" in stringAnalysis}\n")

# The replace method is a way way of replace a content to another.
print(f"This what happens when we use the \"replace\" method to replace the word \"analysis\" for \"study\": {stringAnalysis.replace("analysis", "study")}\n")

# It is possible to turn lowercase text into uppercase strings using the "upper" method
print(f"Everything is in uppercase: {stringAnalysis.upper()}\n")

# It is possible to turn uppercase text into lowercase strings using the "lower" method
print(f"Everything is in lowercase: {stringAnalysis.lower()}\n")

# Capitalization of the first character in a sentence it's completely possible thankfully to the "capitalize" method
print(f"See how it looks our string when we use the capitalize method: {stringAnalysis.capitalize()}\n")

# There is also another interesting method called "title" that you can use to kind of capitalize the first character of each word based on the whitespace before the word
print(f"This is how it looks like using the \"title\" method: {stringAnalysis.title()}\n")

# Now let's suppose you are asking an user to input their name and the user make the mistake of pressing the space key a few times before actually typing in your age, you can get rid of this space using the "strip" method
print(f"This is what we have before the \"strip\" method: {userAgeInput}")
print(f"Now strip that string: {userAgeInput.strip()}")
print(f"Can't you see what happened? What if I replace the whitespaces for this \"×\" characters?\nBefore: {userAgeInput.replace(" ", "×")}\nAfter: {userAgeInput.strip()}\n")

# Now let's suppose you want the start "stripping" from the right side or left side, you could use the "lstrip" or "rstrip" methods
print(f"For example, given this string: {userAgeInput}")
print(f"Let's remove the whitespaces on the right side: {userAgeInput.rstrip()}")
print(f"And finally let's remove the whitespaces on the left side: {userAgeInput.lstrip()}\n")

# We can split a string into different lists (automatically changing the indexes of the items inside the list)
print(f"Here's a split of: {stringAnalysis.split()}\n")

# By the way you can join a string into another
print(f"So, we have this Serial Number: {serialNumber}\nLet's use the \"join\" method to add the number 5 all over for our serial number: {"5".join(serialNumber)}\n")

# There is also the possibility of mixing methods because in Python everything is an object
print(f"""For example, if we combine the \"upper\", \"lstrip\" and \"replace\" to do this:
1 - Transform the whole string into uppercase
2 - Strip the whitespaces on the left side of our string
3 - Replace the whitespaces on the right side of our string by \"×"\ characters
This is what we get: {userAgeInput.upper().lstrip().replace(" ", "×")}""")

''' 
When you use replace you are not ACTUALLY replacing a value inside of a string because strings are actually immutable so let's learn what's really happening
When you use the "replace" method you are basically creating an alternative instance of the targeted string on your memory, it is like temporarily maintaining a modified clone of your first string in your memory
'''
print("When you use replace you are not ACTUALLY replacing a value inside of a string because strings are actually immutable so let's learn what's really happening!")
print("When you use the \"replace\" method you are basically creating an alternative instance of the targeted string on your memory, it is like temporarily maintaining a modified clone of your first string in your memory")
print(f"For example, this our Serial Number: {serialNumber}\nAnd this our instanced version of our Serial Number using the \"replace\" method {serialNumber.replace(" ", "-")}\n")
print("However, once you check the value of our Serial Number again, you can see it is without hyphens, and that is because our replace method created a temporary instance of your original string")
print("To change this, you can use attribution, like this \"serialNumber = serialNumber.replace(\" \", \"-\")\" this would replace the original value of our previous string and not only instance a new one temporarily.")
serialNumber = serialNumber.replace(" ", "-")

print(f"Serial Number: {serialNumber}")
