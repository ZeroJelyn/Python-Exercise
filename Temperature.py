def check_temp(temperature):
    if float(temperature )< 37.5:
        print("Normal temperature.")
    elif float(temperature) < 39.:
        print ("Fever.")
    else:
       print("High fever.")
       print("Covid-19.")

# Example usage
temperature = float(input("Enter your temperature: "))
print(check_temp(temperature))