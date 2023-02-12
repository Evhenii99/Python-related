# def get_age(year_of_birth, current_year=2023):
#     age = current_year - year_of_birth
#     return age
#
#
# birth = int(input("What is your year of birth?: "))
# age = get_age(birth)
#
# if age <= 120:
#     print(age)
# else:
#     print("You are too old!")

# def count_names(name_list_local):
#     list_count = name_list_local.split(',')
#     return len(list_count)
#
#
# name_list = input("Enter names separated by commas (no spaces): ")
# nr_items = count_names(name_list)
# print(nr_items)

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
