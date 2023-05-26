import statistics
import collections

arr = [1, 9, 3, 2, 3, 7, 6, 5, 8, 9, 1, 10]

print("Max: %d\nMin: %d\nMean: %d\nMedian: %d" % (max(arr), min(arr), statistics.mean(arr), statistics.median(arr)))
print("Frequency: " + str(collections.Counter(arr)))
print("Mode: %d" % (statistics.mode(arr)))