# Python Weight Converter.

weight = float(input("Enter your weight : "))
unite = input("Kilograms or pound (enter k or l) : ")

if unite.lower() == "k" :
    weight = weight * 2.205
    unite = "lbs"
    print(f"Your weight is {round(weight,1)} {unite}")

elif unite.lower() == "l" :
    weight = weight / 2.205
    unite = "kg"
    print(f"Your weight is {round(weight,1)} {unite}")

else:
    print(f"Your {unite} is not valid")