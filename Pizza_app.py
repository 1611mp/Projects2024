
pizza = {"Veg Extravaganza":50, "Mexican Greenwave":65, "Achari Paneer":70, "Chicken Tikka":90}
for item,cost in pizza.items():
    print(item,cost)

pizza_order = input("Please Input  Order of your choice (comma-separated): ").title()
selected_pizza_list = pizza_order.split(',')

total_cost = 0

for pizza_name in selected_pizza_list:
    if pizza_name in pizza:
        total_cost += pizza[pizza_name]
        print(f"You Chose {pizza_name}. It costs {pizza[pizza_name]}$")
    else:
        print(f"We don't have {pizza_name} in our menu.")

print(f"Total cost for your order is {total_cost}$")

