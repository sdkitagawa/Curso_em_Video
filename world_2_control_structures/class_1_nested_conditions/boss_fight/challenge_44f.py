'''
Develop a program that calculates the amount to be paid for a product. Considering its normal price and payment terms:

- Cash/check: 10% discount;
- Cash on card: 5% discount;
- Up to 2x by credit card: Normal price;
- 3x or more on the credit card: 20% interest.

'''

product_price = float(input("\nWelcome to the CiV Labs!\n\nThis is the Multi-Method Price Calculator\nPlease enter the price for your product: "))
payment_method = int(input("\nNow, enter the payment method of your preference:\n\n1 - Cash/Check (10% of discount)\n2 - Cash on card (5% of discount)\n3 - Up to 2x by Credit Card: Normal\n4 - 3x or more on the Credit Card (20% interest)\n\nPayment Method: "))
print(f"\nAlright, I heard you! ", end = "")

if payment_method > 4:
    print("But this payment method is not available... ( •_•)")
elif payment_method == 1:
    discount_price = product_price * 0.1
    final_price = product_price - discount_price
    print(f"The final price of the product is: ${final_price:.2f}")
elif payment_method == 2:
    discount_price = product_price * 0.05
    final_price = product_price - discount_price
    print(f"The final price of the product is: ${final_price:.2f}")
elif payment_method == 3:
    print(f"The final price of the product is: ${product_price:.2f}")
else:
    price_increase = product_price * 0.2
    final_price = product_price + price_increase
    print(f"The final price of the product is: ${final_price:.2f}")
