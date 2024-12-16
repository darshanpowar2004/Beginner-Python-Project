# Concession stand program

menu = {"Rice":60,
        "Dal":100,
        "Cooking Oil":120,
        "Sugar":45,
        "Milk":29,
        "Tea powder":300}

cart = []
total_bill = 0

print("__________MENU__________")
for key,value in menu.items():
    print(f"{key:15} : ₹{value:.2f}")
print("_________________________")

while True:
        item = input("Select an item (q to quit) : ").capitalize()
        if item == "Q":
                break
        elif menu.get(item) is not  None:
                cart.append(item)
                total_bill += (menu.get(item))

print("_________________________")
print("Cart : ",end="")
for item in cart:
        print(item,end=" ")
print()

print(f"Total = ₹{total_bill}")

print("_________________________")
