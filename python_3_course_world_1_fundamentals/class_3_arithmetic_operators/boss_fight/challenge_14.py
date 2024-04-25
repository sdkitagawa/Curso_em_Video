'''
Write a program that converts a temperature entered in ºC (Celsius) and converts it to ºF (Fahrenheit)

'''

temperatureCelsius = float(input("Please enter the temperature in Celsius "))
convertToFahrenheit = 9 * temperatureCelsius / 5 + 32
print(f"The temperature of {temperatureCelsius}ºC (degrees Celsius) is equal to {convertToFahrenheit}ºF (degrees Fahrenheit)")
