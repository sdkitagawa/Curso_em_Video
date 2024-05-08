'''
Develop an algorithm that reads the price of a product and displays its price with a 5% discount.


'''

productPrice = float(input("Please enter the product price: "))
desiredDiscount = float(input("Now, please enter the desired discount that you want to apply on top of the full price: "))
discountPrice = productPrice * desiredDiscount
finalPrice = productPrice - discountPrice
print(f"You are having a discount of ${discountPrice}\nThe price of the product with {desiredDiscount:.2f}% of discount is ${finalPrice}")
