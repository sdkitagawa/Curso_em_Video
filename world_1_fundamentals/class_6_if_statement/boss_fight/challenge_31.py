'''
Develop a program that asks the distance of a journey in km.

Calculate the ticket price, charging R$0.50 per kilometers for journeys of up to 200 kilometers and R$0.45 for longer journeys.

'''

distanceKilometers = float(input("\nWelcome to the CiV Labs!\n\nThis is the Fare Fee Calculator\n\nEnter the number of kilometers: "))
normalPrice = float(0.50)
discountPrice = float(0.45)
tripPricing = float(distanceKilometers * normalPrice)
travelPricing = float(distanceKilometers * discountPrice)
discountTrigger = float(200)

if distanceKilometers <= discountTrigger:
    print(f"\nAlright! Have a nice trip!\n\nThe price of your ticket is: ${tripPricing:.2f}")
else:
    print(f"\nWow! That's definitely not a trip! More like a Travel, right?\n\nThe price of your ticket is: ${travelPricing:.2f}")
