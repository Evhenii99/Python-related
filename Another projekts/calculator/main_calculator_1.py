run = True

while run:
    what_todo = input("What do you want to do?\n1 for +\n2 for -\n3 for *\n4 for /\n: ")

    def mathematical_operation():
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        if what_todo == '1':
            result = first_number + second_number
        elif what_todo == '2':
            result = first_number - second_number
        elif what_todo == '3':
            result = first_number * second_number
        elif what_todo == '4':
            result = first_number / second_number
        print(f"Answer is {result}")

    match what_todo:
        case '1':
            mathematical_operation()
        case '2':
            mathematical_operation()
        case '3':
            mathematical_operation()
        case '4':
            mathematical_operation()
        case _:
            print("Your value in not 1-4")

    user_input = input("Do you want to continue? Enter Yes or No: ")
    user_input = user_input.capitalize()
    if user_input == 'Yes':
        run = True
    else:
        break
print("Thank for using this program, have a nice day!")