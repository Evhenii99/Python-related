new = True

while new:
    user_actions = input("Choice your number: 1 for +, 2 for -, 3 for *, 4 for /: ")
    user_actions = user_actions.strip()

    match user_actions:
        case '1':
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            result = first_number + second_number
            print(f"Answer is {result}")
            user_input = input("Do you want to continue? Enter Yes or No: ")
            user_input = user_input.capitalize()
            if user_input == 'Yes':
                new = True
            else:
                break
        case '2':
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            result = first_number - second_number
            print(f"Answer is {result}")
            user_input = input("Do you want to continue? Enter Yes or No: ")
            user_input = user_input.capitalize()
            if user_input == 'Yes':
                new = True
            else:
                break
        case '3':
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            result = first_number * second_number
            print(f"Answer is {result}")
            user_input = input("Do you want to continue? Enter Yes or No: ")
            user_input = user_input.capitalize()
            if user_input == 'Yes':
                new = True
            else:
                break
        case '4':
            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))
            result = first_number / second_number
            print(f"Answer is {result}")
            user_input = input("Do you want to continue? Enter Yes or No: ")
            user_input = user_input.capitalize()
            if user_input == 'Yes':
                new = True
            else:
                break
        case _:
            print("Hey, you entered an unknown command")
print("Have a nice day!")
