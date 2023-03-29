from statistics import mean, median, mode
from collections import Counter

#TASK 1
ages = [32, 31, 30, 37, 37, 33]
earnings = [1270, 7980, 4700, 1810, 570, 1100]

print("Min: %d;%d\nMax: %d;%d\nMean: %d;%d" % (min(ages), min(earnings), max(ages), max(earnings), mean(ages), mean(earnings),))

#TASK 2
arr = [1, 9, 3, 2, 3, 7, 6, 5, 8, 9, 1, 10]

print("Min: %d\nMax: %d\nMean: %d\nMedian: %d\nFreq: %s\nMode: %d" % (min(arr), max(arr), mean(arr), median(arr), str(Counter(arr)).replace("Counter({", "").replace("})", "") , mode(arr)))

#TASK 3
arr1 = [2, 10, 16, 17, 29, 47, 7]
arr2 = [8, 11, 26, 27, 38, 45, 43]
arr3 = [2, 9, 11, 35, 36, 44, 12]

print(str(Counter(arr1 + arr2 + arr3)).replace("Counter({", "").replace("})", ""))

#TASK 4
file = open("text.txt", "r")
text = file.read().split()
file.close

print("Top 20 words:")
 
for item in Counter(text).most_common(20):
    print(str(item).replace("(", "").replace(",", ":").replace(")", ","))