unit =  input("The temperature is Celsius or Fahrenheit ( C or F ) : ")
temp = float(input("Enter your temperature : "))

if unit.lower() == "c":
    temp = (temp * (9/5)) + 32
    unit = "°F"
    print(f"The temperature in Fahrenheit is {round(temp,1)} {unit}")

elif unit.lower() == "f" :
    temp = (temp - 32) * (5/9)
    unit = "°C"
    print(f"The temperature in Celsius is {round(temp,1)} {unit}")


else:
    print(f"your '{unit}' is not valid unite.")