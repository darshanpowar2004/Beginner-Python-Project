# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q for quite) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food} : "))
        foods.append(food)
        prices.append(price)
        total += price

print("_____ YOUR SHOPPING CART _____")

for food,price in zip(foods,prices):
    print(f"{food} = ₹{price}")

print()

gst = float(total*(5/100))
print(f"GST = {gst}")

print(f"Total = {float(total+gst)} with GST")