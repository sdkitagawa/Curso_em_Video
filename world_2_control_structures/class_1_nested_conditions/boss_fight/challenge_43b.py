'''
Develop a logic that reads a person's weight and height, calculates their BMI and displays their status, according to the table below:

- Below 18.5: Underweight;
- Between 18.5 and 25: Ideal weight;
- 25 to 30: Overweight;
- Over 40: Morbidly obese.

'''

patient_name = str(input("Welcome to the CiV Labs\n\nThis is the BMI Calculator\nPlease enter the patient's name: "))
user_weight = float(input("\nPlease insert your weight (in Kilograms): "))
user_height = float(input("\nPlease insert your height (in Centimeters): "))

print(f"\nThe BMI of {patient_name} is equals to {user_weight / (user_height * user_height):.2f}.")
print(f"\nPatient {patient_name} is ", end = "")

if user_weight / (user_height * user_height) <= 18.5:
    print("Underweight.")
elif user_weight / (user_height * user_height) > 18.5 and user_weight / (user_height * user_height) <= 25:
    print("at your Ideal weight.")
elif user_weight / (user_height * user_height) > 25 and user_weight / (user_height * user_height) <= 30:
    print("Overweight.")
elif user_weight / (user_height * user_height) > 30 and user_weight / (user_height * user_height) <= 40:
    print("Obese.")
else:
    print("Morbidly obese.")
