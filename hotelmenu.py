# # Define the menu for the Restaurant
# menu = {
#     'pizza':180,
#     'burger':100,
#     'pasta':150,
#     'salad':120,
#     'soda':50
# }

# # Greet the user 
# print("Welcome to our Python Restaurant!")
# print("Here is our menu:")
# for item, price in menu.items():
#     print(f"{item.capitalize()}: ${price}")

# order_total = 0

# item_1 = input("Please enter the first item you would like to order: ").strip().lower()
# if item_1 in menu:
#     order_total += menu[item_1] 
#     print(f"{item_1.capitalize()} added to your order.")
# else:
#     print(f"Sorry, we don't have {item_1} on the menu.")

# another_order = input("Anything else? Please enter the second item(Yes/No): ").strip().lower()
# if another_order == 'yes':
#     item_2 = input("Please enter the second item you would like to order: ").strip().lower()
#     if item_2 in menu:
#         order_total += menu[item_2] 
#         print(f"{item_2.capitalize()} added to your order.")
#     else:
#         print(f"Sorry, we don't have {item_2} on the menu.")

# print(f"Your total order amount is: ${order_total}")
# print("Thank you for dining with us!")

# Define the menu for the Restaurant
menu = {
    'pizza':180,
    'burger':100,
    'pasta':150,
    'salad':120,
    'soda':50
}

# Greet the user 
print("Welcome to our Python Restaurant!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item.capitalize()}: ${price}")

order_total = 0

while True:
    item = input("Please enter the item you would like to order (or type 'done' to finish): ").strip().lower()
    
    if item == 'done':
        break
    elif item in menu:
        order_total += menu[item]
        print(f"{item.capitalize()} added to your order.")
    else:
        print(f"Sorry, we don't have {item} on the menu.")

print(f"Your total order amount is: ${order_total}")
print("Thank you for dining with us!")