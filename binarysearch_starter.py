import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)

# Start your search algorithm here.
#
#RECURSIVE VERSION
#def binarySearch(alist, item):
#     if len(alist) == 0:
#         return -1
#     else:
#         midpoint = len(alist)//2
#         if alist[midpoint]==item:
#             return midpoint
#         else:
#             if item<alist[midpoint]:
#                 return binarySearch(alist[:midpoint], item)
#             else:
#                 return binarySearch(alist[midpoint+1:],item)

def binarySearch(alist, item): #defnes algorithm
    first= 0 #defines variable that sets the lower limit of the list
    last = len(alist)-1 #defines the upper limit of the list. Gets the length of the list minus one
    found = False #sets a boolean that will force the function to find the word as it is set to false


    while first<=last and not found: #while you're in the list and you haven't found the item:
        midpoint = (first + last)//2 #sets the midpoint
        if alist[midpoint] == item:# if the word you're looking for is the midpoint, you've found the word
            found = midpoint
        else: #if the word you're looking for isn't the midpoint:
            if item < countries[midpoint]: #if the word you're lookng for is less than the midpoint
                last = midpoint-1 # change the midpoint to one point down and set it as the last variable, then run through the while loop again, making it check through the first half of the list
            else: #if the word you're looking for is greater than the midpoint:
                first = midpoint + 1 #set the first value at one point greater than the midpoint, making it go through the while loop again, starting after the midpoint
    return found


searched = binarySearch(countries, 'USA')
if searched == False:
    print ("country not found")
else:
    print (searched)
