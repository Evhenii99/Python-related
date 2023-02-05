with open("D:\Development\Python\section 11 - File Processing/vegetables.txt", "a+") as myfile:
    myfile.write("\nOnion")
    myfile.seek(0)
    content = myfile.read()

print(content)