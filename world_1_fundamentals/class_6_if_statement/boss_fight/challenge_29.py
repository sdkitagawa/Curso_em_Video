'''
Write a program that reads the speed of a car. 

If the car exceeds 80km/h, display a message saying that it has been fined.

The fine will cost $7.00 for each kilometer over the limit.

'''

trackedSpeed = float(input("\nWelcome to the CiV Labs!\n\nThis is the CiV Labs Radar System.\n\nEnter the car speed: "))
acceptableSpeed = float(80)
exceededKilometers = trackedSpeed - acceptableSpeed
trafficFine = exceededKilometers * 7

if trackedSpeed > acceptableSpeed:
    print(f"\nThe car has exceeded the acceptable speed of {acceptableSpeed}km/h!\n\nThe amount of the fine is: ${trafficFine:.2f}")
else:
    print("The car was within the speed limit. Please keep driving with safety!")
