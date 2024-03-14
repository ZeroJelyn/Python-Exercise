citizen = input("Enter your citizenship: ")
age = int(input("Age: "))

if citizen == "Malaysia" and age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")