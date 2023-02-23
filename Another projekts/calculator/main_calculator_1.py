from functions import mathematical_operation

while True:
    what_todo = input("What do you want to do?\n1 for +\n2 for -\n3 for *\n4 for /\n: ")

    mathematical_operation(what_todo)

    user_input = input("Do you want to continue? Enter Yes or No: ")
    user_input = user_input.capitalize()
    if user_input == 'Yes':
        continue
    else:
        break
print("Thank for using this program, have a nice day!")
