# TASK 1
# favArtist = str(input("Type your favorite artist's name: "))
# compliment = favArtist + " is brilliant!"
# print(compliment)

# TASK 2
# name = str(input("Type your full name: "))

# fName = name.split(" ")[0]
# sName = name.split(" ")[1]

# print(fName)
# print(sName)

# TASK 3
# time = str(input("Type your time (HH:mm:ss): "))
# hours = int(time.split(":")[0]) * 60 * 60
# minutes = int(time.split(":")[1]) * 60
# seconds = int(time.split(":")[2])
# totalSeconds = hours + minutes + seconds

# print(totalSeconds)

# TASK 4
# seconds = int(input("Type a five digit number representing seconds: "))
# minutes = round(seconds / 60)

# print(minutes)

# TASK 5
# userInput = str(input("Type 5 random characters: "))
# characters = []

# for i in range (0, 5):
#     characters.append(ord(userInput[i]))
#     print(ord(userInput[i]))

# TASK 6
# electricityUsed = int(input("Type number of units of electricity used in a month: "))
# electricityCost = 0.19
# standingCharge = 26.20

# print("Electricity debt: %.2f€" % ((electricityUsed * electricityCost) + standingCharge))

# TASK 7
# fishPortions = int(input("Type amount of fish portions: "))
# chipsPortions = int(input("Type amount of chips portions: "))
# chipsPrice = 2.80
# fishPrice = 4.50
# totalPrice = (fishPortions * fishPrice) + (chipsPortions * chipsPrice)

# print("Your order: %d chips portions and %d fish portions\nTotal price: %.2f€\nVAT charged: %.2f€" % (chipsPortions, fishPortions, totalPrice, (totalPrice * 9)/100))

# TASK 8
# word = str(input("Type your word: ")).lower()
# shiftKey = int(input("Type your shift key: "))
# encryptedWord = ""

# if(shiftKey > 25 or shiftKey < 0):
#     print("Invalid entry")
# else:
#     for i in range(0, len(word)):
#         encryptedWord += chr(ord(word[i]) + shiftKey)
#     print("Input: %s;\nKey: %d;\nOutput: %s" % (word, shiftKey, encryptedWord))
