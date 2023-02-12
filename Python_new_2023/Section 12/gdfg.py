users_input = input("Enter a string: ")


def scrolling_text(string: str) -> list:
    string = string.upper()
    result_list = []
    for i in range(len(string)):
        result_list.append(string[i:] + string[:i])
    return result_list


print(scrolling_text(users_input))
