# user_entered = int(input("Enter number: "))
#
#
# def is_jumping(number: int) -> str:
#     prev_digit = number % 10
#     number //= 10
#     while number > 0:
#         if abs(prev_digit - number % 10) != 1:
#             return "NOT JUMPING"
#         prev_digit = number % 10
#         number //= 10
#     return "JUMPING"
#
#
# print(is_jumping(user_entered))
# number = int(input("Enter number: "))
#
#
# def is_special_number(number_local: int) -> str:
#     while number_local > 0:
#         if number_local % 10 > 5:
#             return "NOT!!"
#         number_local //= 10
#     return "Special!!"
#
#
# print(is_special_number(number))
