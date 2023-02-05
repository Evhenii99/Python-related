myfile = open("d:/Development/Python/section 11 - File Processing/fruits.txt")
content = myfile.read()
myfile.close()

with open("d:/Development/Python/section 11 - File Processing/fruits.txt") as myfile:
    content = myfile.read()

print(content)