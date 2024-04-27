'''
Develop a program that reads the name of a city and tells you whether or not it begins with the name "SANTO".

'''

print("\nWelcome to the CiV Labs!\n\nThis is a software developed to check if the word \"SANTO\" is present in a city name!\n")
cityName = str(input("Enter a city name: ")).upper().strip()

print(f"Is the word \"Santo\" present in city's name: {cityName[:5] == "SANTO"}")
