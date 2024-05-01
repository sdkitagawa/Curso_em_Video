'''
If Statement

Themes:
 - Simple
 - Compound

'''

sexDefinition = str(input("Are you a boy o a girl?\n\n"))

nameInput = str(input("\nWhat's your name?\n\n"))
bestMaleName = str("daisuke")
bestFemaleName = str("midori")
sexMale = str("boy")
sexFemale = str("girl")

print(sexDefinition)
print(nameInput)

if sexDefinition == sexMale:
    if nameInput == bestMaleName:
        print(f"\nYou have a great name Mr. {nameInput.capitalize()}!")
else:
    if nameInput == bestFemaleName:
        print(f"\nYou have a great name Ms. {nameInput.capitalize()}!")
print(f"\nI hope you have an amazing day {nameInput.capitalize()}!")
