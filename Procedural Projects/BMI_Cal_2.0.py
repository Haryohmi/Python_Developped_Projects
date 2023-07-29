print("welcome to BMI 2.0 calculator")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
Bmi = weight / (height * height)
# print(Bmi)
result = round(Bmi)
if Bmi < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif Bmi < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif Bmi < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif Bmi < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obsese.")