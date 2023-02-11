def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    min_grade = min(grades)
    output = f"Max: {max_grade}, Min: {min_grade}"
    return output


print(get_max())


def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum = max(celsius_local)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
