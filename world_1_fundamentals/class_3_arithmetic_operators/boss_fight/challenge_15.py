'''
Write a program that asks for the number of kilometers a rental car has traveled and the number of days it has been rented for. Calculate the price to pay, knowing that the car costs $60 per day and $0.15 per kilometers driven.

'''

daysRented = int(input("Enter the amount of days that you would like to rent the car for: "))
kilometersDriven = float(input("How many kilometers have you driven the car: "))
dailyPrice = (daysRented * 60) + (kilometersDriven * 0.15)
print(f"The total amount to be paid is ${dailyPrice:.2f}")
