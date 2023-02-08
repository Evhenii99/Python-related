# password = input("Enter a new password: ")

# if len(password) > 7:
#    print("Great password there!")
# elif len(password) == 7:
#    print("Password is OK, but not too strong")
# else:
#    print("Your password is weak.")

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")
