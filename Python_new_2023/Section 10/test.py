# try:
#    total_value = float(input("Enter total value: "))
#    value = float(input("Enter value: "))

#    result = value / total_value * 100
#    print(f"This is {result}%")
# except ValueError:
#    print("You need to enter a number. Run the program again")
# except ZeroDivisionError:
#    print("Your total value cannot be zero.")

waiting_list = ["john", "marry"]
name = input("Enter name: ")

try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")
