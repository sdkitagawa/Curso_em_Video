'''
Create an algorithm that reads an employee's salary and displays their name and salary, with a 15% increase.

'''

personsSalary = float(input("Please enter the person's current salary: "))
calculateSalary = personsSalary * 1.015
print(f"This is the person's salary after a 15% raise ${calculateSalary:.2f}")
