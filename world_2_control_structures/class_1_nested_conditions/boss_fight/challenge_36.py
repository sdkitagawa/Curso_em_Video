'''
Develop a program to approve a bank loan to buy a house. The program will ask for the value of the house, the buyer's salary and how many years they will pay.

Calculate the monthly installment, knowing that it cannot exceed 30% of the salary or the loan will be denied.

'''

house_valuation = float(input("\nWelcome to the CiV Labs!\nThis is the Financial Loan System for Real Estate Purchase\nCould you please enter the Value of the House: "))
buyers_salary = float(input("\nExcellent! Now, could you please type your salary: "))
number_of_years = int(input("\nThings are pretty much well so far! How many years do you intend to pay for this house: "))
years_to_installments = number_of_years * 12
amount_per_installment = house_valuation / years_to_installments
exceeded_trigger = buyers_salary * 0.3

if exceeded_trigger > amount_per_installment:
    print(f"\nWe'd be delighted to give you this loan sir!\nLoan approved!\n\nYou will pay {years_to_installments} installments of ${amount_per_installment:.2f} for {number_of_years} years")
else:
    print("\nUnfortunately this loan couldn't be approved. We're really sorry about this.")
