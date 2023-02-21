def mathematical_operation(choise):
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    if choise == '1':
        result = first_number + second_number
        print(f"The answer is {result}")
    elif choise == '2':
        result = first_number - second_number
        print(f"The answer is {result}")
    elif choise == '3':
        result = first_number * second_number
        print(f"The answer is {result}")
    elif choise == '4':
        result = first_number / second_number
        print(f"The answer is {result}")
    else:
        print(f"Your value in not 1-4")