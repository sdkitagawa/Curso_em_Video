'''
Develop an algorithm that reads the price of a product and displays its price with a 5% discount.

'''

productPrice = float(input("Please enter the product price: "))
discountPrice = productPrice * 0.5
finalPrice = productPrice - discountPrice
print(f"The price of the product with a 5% discount is ${finalPrice}")
