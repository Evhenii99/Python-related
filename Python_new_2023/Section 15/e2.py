import csv

with open("weather.csv", "r") as file:
    date = list(csv.reader(file))

city = input("Enter a city: ")

for row in date[1:]:
    if row[0] == city:
        print(row[1])
