import random
import csv

arr = []
for i in range(0, 20):
    arr.append(random.randint(1, 50))
arr.sort(reverse=False)

with open('q2.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file.writerow(arr)

def findMax(array):
    currentMax = 0
    for i in range(0, len(array)):
        if(array[i] > currentMax): currentMax = array[i]
    
    return currentMax

def findMin(array):
    currentMin = 9999
    for i in range(0, len(array)):
        if(array[i] < currentMin): currentMin = array[i]
    
    return currentMin

print("Max: %d\nMin: %d" % (findMax(arr), findMin(arr)))