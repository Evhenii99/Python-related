import time
import os
import pandas

while True:
    if os.path.exists("D:\Development\Python\section 12 - Modules/temps_today.csv"):
        data = pandas.read_csv("D:\Development\Python\section 12 - Modules/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)