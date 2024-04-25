# Build a program that reads an integer and displays its successor and predecessor on the screen.

userNumber = int(input("Type the number: "))
successorNumber = userNumber + 1
predecessorNumber = userNumber - 1

print(f"Your number is {userNumber}\nIts Successor is {successorNumber}\nIts Predecessor is {predecessorNumber}")
