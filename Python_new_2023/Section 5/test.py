ips = ['100.122.133.105', '100.122.133.111']

user_input = int(input("Enter the index of the IP you want: "))
print(f"You chose {ips[user_input]}")

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")