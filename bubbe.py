import csv
import string

# Open the CSV File and read it in.
f = open('names.csv')
data = f.read()

# Split the data into an array of countries.
names = data.split('\n')

length = len(names)

for cyc in range(length-1):
    for i in range(length-cyc -1):
        if (names[i] > names[i+1]):
            temp = names[i]
            names[i] = names[i+1]
            names[i+1] = temp

print(names)
