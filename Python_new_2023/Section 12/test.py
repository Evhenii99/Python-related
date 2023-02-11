# while True:
#     litters_input = int(input("Enter litters to convert: "))
#
#
#     def convert(liters):
#         result = liters / 1000
#         return result
#
#
#     print(convert(litters_input))


user_password = input("Enter new password: ")


def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False
    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong password"
    else:
        return "Weak password"


print(strength(user_password))
