#TASK 1
# age = int(input("Enter your age: "))
# score = int(input("Enter your score: "))

# if(age <= 16 and score >= 80):
#     print("Excelent!")
# elif(age > 16 and score >= 80):
#     print("Good!")
# else:
#     print("Please try harder next time!")

#TASK 2
# orderQuantity = int(input("Enter your order quantity: "))
# customerStatus = input("Are you a Gold Member? (Y/N) ")
# discount = 0.0

# if(orderQuantity >= 25 and orderQuantity < 100): discount += 5.0
# elif(orderQuantity >= 100): discount += 10.0

# if(customerStatus.lower() == "y"): discount += 3.5
# print(discount)

#TASK 3
# monthOfBirth = input("Enter your month of birth: ")

# if(monthOfBirth.lower().startswith("sep")):
#     print("There are 12 months until your birthday")
# elif(monthOfBirth.lower().startswith("oct")):
#     print("There are 11 months until your birthday")
# elif(monthOfBirth.lower().startswith("nov")):
#     print("There are 10 months until your birthday")
# elif(monthOfBirth.lower().startswith("dec")):
#     print("There are 9 months until your birthday")
# elif(monthOfBirth.lower().startswith("jan")):
#     print("There are 8 months until your birthday")
# elif(monthOfBirth.lower().startswith("feb")):
#     print("There are 7 months until your birthday")
# elif(monthOfBirth.lower().startswith("mar")):
#     print("There are 6 months until your birthday")
# elif(monthOfBirth.lower().startswith("apr")):
#     print("There are 5 months until your birthday")
# elif(monthOfBirth.lower().startswith("may")):
#     print("There are 4 months until your birthday")
# elif(monthOfBirth.lower().startswith("jun")):
#     print("There are 3 months until your birthday")
# elif(monthOfBirth.lower().startswith("jul")):
#     print("There are 2 months until your birthday")
# elif(monthOfBirth.lower().startswith("aug")):
#     print("There are 1 month until your birthday")
# else:
#     print("Sorry, can't find any data for you ;c")

#TASK 4
# mopedType = input("Enter your mopped's type: ")
# dayOfRent = input("Enter the day of rent: ")
# time = int(input("Enter the number of hours it's rented for: "))
# price = 0

# if(time < 0):
#     print("Error! Time can't be 0!")

# if(dayOfRent.lower().startswith("sun") or dayOfRent.lower().startswith("sat")):
#     if(mopedType.startswith("250")):
#         for i in range(0, time):
#             if(i < 3):
#                 price = 35
#             else:
#                 price += 5
#     else:
#         for i in range(0, time):
#             if(i < 3):
#                 price = 30
#             else:
#                 price += 3
# else:
#     if(mopedType.startswith("250")):
#         for i in range(0, time):
#             if(i < 3):
#                 price = 25
#             else:
#                 price += 3.5
#     else:
#         for i in range(0, time):
#             if(i < 3):
#                 price += 15
#             else:
#                 price += 2.5

# print(price)

#TASK 5
# email = input("Enter your email: ")

# if(len(email) >= 8):
#     try:
#         email.index("@")
#         email.index(".")
#     except ValueError:
#         print("Enter a valid email!")
#     else:
#         print("Success!")
# else:
#     print("Your email is too short! Enter a valid email!")

# TASK 6
# level = input("Enter your level (O/H): ")
# marks = int(input("Enter your mark: "))

# def levelGen(lvl, mrk):
#     if(mrk < 0 or mrk > 100):
#         return print("Error")

#     if(mrk < 30):
#         grade = lvl + "1"
#     elif(mrk > 30 and mrk < 40):
#         grade = lvl + "2"
#     elif(mrk > 40 and mrk < 50):
#         grade = lvl + "3"
#     elif(mrk > 50 and mrk < 60):
#         grade = lvl + "4"
#     elif(mrk > 60 and mrk < 70):
#         grade = lvl + "5"
#     elif(mrk > 70 and mrk < 80):
#         grade = lvl + "6"
#     elif(mrk > 80 and mrk < 90):
#         grade = lvl + "7"
#     elif(mrk == 100):
#         grade = lvl + "8"
        
#     return grade

# if(level.lower() == "o" or level.lower() == "h"):
#     print(levelGen(level, marks))

# TASK 6
# lines = []

# for i in range (0, 3):
#     lines.append(int(input("Enter line #%d: " % (i + 1))))

# def getPythagor(sticks):
#     c = max(sticks)
#     sticks.remove(c)

#     if(sticks[0]**2 + sticks[1]**2 == c**2):
#         return True # Example: 4, 3, 5
#     else:
#         return False

# print(getPythagor(lines))