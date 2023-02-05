import time
import os

while True:
    if os.path.exists("D:\Development\Python\section 12 - Modules/vegetables.txt"):
        with open("D:\Development\Python\section 12 - Modules/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)