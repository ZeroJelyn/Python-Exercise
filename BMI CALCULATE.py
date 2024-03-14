import random
def complexCalc(weight, height):
        weight = float(weight)
        height = float(height)
        bmi = weight / (height ** 2)
        return bmi

weight = input("Enter your weight in kilograms(kg): ")
height = input("Enter your height in meters(m): ")

def categorize_bmi(bmi):
    if bmi<18.5:
        category="underweight"
    elif 18.5<= bmi<24.5:
       category="Normal"   
    elif bmi>30:
        category="overweight"
    else:
        category="obese"

bmi_result = complexCalc(weight, height)
Category=categorize_bmi(bmi_result)
print("Your bmi results: ", bmi_result)
print("Your category: ",categorize_bmi)

health_Quotes=["A healthy outside starts from the inside.","The key to a healthy life is having a healthy mind","If you keep good food in your fridge, you will eat good food","et food be thy medicine and medicine be thy food","Physical fitness is the first requisite of happiness","Your body hears everything your mind says"]

random_index=random.randint(0,len(health_Quotes)-1)
random_health_Quotes=health_Quotes[random_index]

print(f"List of health quotes:\f",random_health_Quotes)
