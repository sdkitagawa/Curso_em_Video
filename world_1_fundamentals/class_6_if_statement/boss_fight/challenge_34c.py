'''
Develop a program that asks for an employee's salary and calculates the amount of their raise.

For salaries above $1250.00, calculate a 10% increase.

For those below or equal to $1250.00, the increase is 15%.

'''

employeeSalary = float(input("\nWelcome to the CiV Labs!\n\nThis is the salary raise calculator 2.0\n\nInsert the value of your salary: "))
if employeeSalary <= 1250:
    totalRaise = employeeSalary + (employeeSalary * 0.1)
    print(f"The employee will receive a 10% raise, resulting in a total salary of: {totalRaise:.2f}")
else:
    totalRaise = employeeSalary + (employeeSalary * 0.15)
    print(f"The employee will receive a 15% raise, resulting in a total salary of: {totalRaise:.2f}")
