import statistics

ages = [32, 31, 30, 37, 37, 33]
earnings = [1270, 7980, 4700, 1810, 750, 1100]

print("AGES\nMax: %d;\nMin: %d\nMean: %d" % (max(ages), min(ages), statistics.mean(ages)))
print("\nEARNINGS\nMax: %d;\nMin: %d\nMean: %d" % (max(earnings), min(earnings), statistics.mean(earnings)))