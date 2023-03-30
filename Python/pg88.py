import matplotlib.pyplot as plt

#TASK 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# plt.ylabel("Label")
# plt.title("Title")
# plt.show()

#TASK 2
#SENSOR FAULT

#TASK 3
# students = ["John Smith", "James Smith", "Michael Smith", "Maria Garcia", "Robert Smith", "David Smith"]
# height = [160, 165, 175, 177, 185, 180]
# plt.plot(students, height, "rs")
# plt.ylabel("Height")
# plt.xlabel("Name")
# plt.title("Title")
# plt.show()

#TASK 4
# students = ["John Smith", "James Smith", "Michael Smith", "Maria Garcia", "Robert Smith", "David Smith"]
# height = [160, 165, 175, 177, 185, 180]
# plt.bar(students, height)
# plt.ylabel("Height")
# plt.xlabel("Name")
# plt.title("Title")
# plt.show()

#TASK 5
# films = ["The Shawshank Redemption (1994)", "The Godfather (1972)", "The Dark Knight (2008)", "The Godfather: Part II (1974)", "12 Angry Men (1957)", "Schindler's List (1993)", "The Lord of the Rings: The Return of the King (2003)", "Pulp Fiction (1994)", "The Lord of the Rings: The Fellowship of the Ring (2001)", "The Good, the Bad and the Ugly (1966)"]
# freq = [5, 1, 4, 0, 0, 1, 4, 0, 5, 0]

# plt.bar(films, freq)
# plt.ylabel("Height")
# plt.xlabel("Name")
# plt.title("Title")
# plt.show()

# plt.pie(freq, labels = films)
# plt.title("Title")
# plt.show()

#TASK 6
# names = ["Lionel Messi", "Steph Curry", "Conor McGregor", "Serena Williams", "Danica Patrick", "Katie Taylor"]
# age = [32, 31, 30, 37, 37, 33]
# earn = [127, 79, 47, 18, 7.5, 1.1]
# agePlot = plt.plot(names, age)
# earnPlot = plt.plot(earn)
# plt.ylabel("Age")
# plt.xlabel("Name")
# plt.title("Title")
# plt.tight_layout()
# plt.show()

#TASK 7
sports = ["Football", "Cricket", "Golf", "Tennis"]
avgMen = [22, 3.1, 1, 1.5]
avgWomen = [0.6, 0.5, 0.5, 1.5]
gap = []

i = 0
while i < 4:
    gap.append(avgMen[i] - avgWomen[i])
    i += 1

menPlot = plt.plot(sports, avgMen)
womenPlot = plt.plot(avgWomen)
plt.ylabel("AVG Prize money")
plt.xlabel("Sport name")
plt.legend(["Men AVG", "Women AVG"])
plt.title("Title")
plt.tight_layout()
plt.show()

plt.pie(gap, labels = sports)
plt.title("GAP 1")
plt.show()

plt.bar(gap, sports)
plt.title("GAP 2")
plt.show()
