'''
Develop a program that reads a sentence from the keyboard and displays it:

- How many times the letter "A" appears

- In which position it appears the first time.

- In which position it appeared the last time.

'''

print("\nWelcome to the CiV Labs!\n\nThis is a Terminal where you can enter a sentence and this sentence will be shown on the LED panel how many times:!\n1 - The Number of times the letter \"A\" is going to appear.\n2 - In which position the letter \"A\" appears the first time.\n3 - In which position the letter \"A\" is going to appear for the last time\n")
userSentence = str(input("Enter your sentence: ")).upper().strip

print(f"1 - Number of times the letter \"A\" appears: {userSentence.count("A")}\n2 - Counting from 0 and going forward the first time that the letter \"A\" appears is: {userSentence.find("A")}\n3 - Counting from 0 and going forward the last time that the letter \"A\" appears is: {userSentence.rfind("A")}")
