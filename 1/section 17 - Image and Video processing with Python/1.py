number_of_guests = 3
def get_drinks(number_of_guests: int) -> int:
    # write your code here
    sum = 0
    for i in range(1, number_of_guests):
        sum += i
        print(sum)
