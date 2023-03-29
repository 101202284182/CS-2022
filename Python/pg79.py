import random
import csv

def genArr(max):
    arr = []
    i = 0

    while i < max:
        arr.append(random.randint(0, max))
        i += 1
    
    return arr

# TASK 1
arr = [1, 2, 3, 4, 5]
i = -len(arr)

while i < len(arr):
    print(arr)
    arr.pop()
    i += 1

#TASK 2
arr = genArr(20)
arr.sort(reverse=True)
with open('pg79_2.csv', mode='w') as file:
    file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(arr)

i = 0
largest_number = 0
while i < len(arr):
    if arr[i] > largest_number:
        largest_number = arr[i]
    i += 1

i = 0
smallest_number = 20
while i < len(arr):
    if arr[i] < smallest_number:
        smallest_number = arr[i]
    i += 1


print("Largest number: %d\nSmallest number: %d" % (largest_number, smallest_number))

# TASK 3
arr = genArr(100)
with open('pg79_3.csv', mode='w', newline='') as file:
    file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(arr)

# TASK 4
with open('pg79_3.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    i = 0
    arr = []
    for row in reader:
        while i < 100:
            if int(row[i]) > 50:
                arr.append(row[i])
            i += 1

with open('pg79_4.csv', mode='w') as file:
    file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(arr)

# TASK 5
with open('pg79_3.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    i = 0
    arr = []
    for row in reader:
        while i < 100:
            if int(row[i]) >= 30:
                arr.append(row[i])
            i += 1

with open('pg79_5.csv', mode='w') as file:
    file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(arr)