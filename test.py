import re

# date = "25/07/1996"

# newDate = date.split("/")

# currentYear = 2023

# convertedYear = int(newDate[2])

# print(currentYear - convertedYear)

# regEx = re.compile(r'^0[0-9]{9}$')
# regEx = re.compile(r'^(?!([0-9])\1{9})0\d{9}$')
regEx = re.compile(r'^[a-zA-Z@]*\d$')
input = input("NEter mobile")

isValid = re.search(regEx, input)

print(isValid)


