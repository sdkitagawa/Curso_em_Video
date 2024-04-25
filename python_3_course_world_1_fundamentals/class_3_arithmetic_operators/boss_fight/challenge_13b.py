'''
Create an algorithm that reads an employee's salary and displays their name and salary, with a 15% increase.

Refactoring:
 - User can now set the percentage of the raise
 - Shows the salary before the raise
 - Shows the raise amount
 - Shows the salary after the raise

'''

personsSalary = float(input("Please enter the person's current salary: "))
percentageRaise = float(input("\nNow, please enter the percentage of the raise by following the sample. ⬇️\n\nFor example, for a raise of \"6,3% = 1.063\".\n\nFor example, for a raise of \"10,38% = 1.1038\"\n\n"))
calculateSalary = personsSalary * percentageRaise
totalRaiseValue = calculateSalary - personsSalary
print(f"\nThis is the person's salary before the raise ${personsSalary:.2f}")
print(f"This is the amount of the raise ${totalRaiseValue:.2f}")
print(f"This is the person's salary after a {percentageRaise}% raise ${calculateSalary:.2f}")
