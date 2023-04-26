import csv
import os

# # TASK 1
# with open('myGarage.csv', 'w', newline='') as csvfile:
#     file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow(["Make", "Model", "Reg"])
#     file.writerow(["Honda", "Civic", "191-D-1234"])
#     file.writerow(["Nissan", "Pulsar", "182-KE-33456"])
#     file.writerow(["Audi", "A8", "201-C-5607"])

# #TASK 2
# with open('myGarage.csv', 'a', newline='') as csvfile:
#     file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow(["Mazda", "Miata", "054-OT-99483"])

# # TASK 3
# userData = []
# for i in range(0, 3):
#     if(i == 0):
#         userData.append(input("Enter car manufacter name: "))
#     elif(i == 1):
#         userData.append(input("Enter car model: "))
#     elif(i == 2):
#         userData.append(input("Enter the license plate: "))

# with open('myGarage.csv', 'a', newline='') as csvfile:
#     file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow([userData[0], userData[1], userData[2]])

# TASK 4
# print("---------myGarage.csv---------\nMake / Model / Reg")
# with open('myGarage.csv', newline='') as csvfile:
#     file = csv.reader(csvfile, delimiter=',', quotechar='"')
#     next(file) # skip header
#     for row in file:
#         print(', '.join(row))
# print("------------------------------")

# #TASK 5
# with open('sommerpass.csv', 'w', newline='') as csvfile:
#     file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow(["Event title", "Date", "City"])
#     file.writerow(["Ü-30 Party Überherrn", "Sun, Apr 30, 2023 20:00 (CEST)", "Überherrn"])
#     file.writerow(["ANOTHERDAY FESTIVAL AT CONTAINER COLLECTIVE MUNICH 20|05|23", "Sat., 20. May 2023 15:00 - Sun., 21. May 2023 05:00 CEST", "München"])
#     file.writerow(["ZEYNEP BASTIK LIVE KONZERT MIT ORCHESTER+MEGA AFTERSHOW PARTY MÜNCHEN!", "Sun 30 Apr 2023 20:00 - Mon 1 May 2023 05:00 CEST", "München"])
#     file.writerow(["Das Rock Orchester bei Kerzenlicht: Wuppertal", "Tue, May 9, 2023 7:00 p.m. (CEST)", "Wuppertal"])
#     file.writerow(["SICKMODE - KINGS OF RAW @DOCKS * * * * *", "Sun, Apr 30, 2023 23:00 (CEST)", "Hamburg"])
#     file.writerow(["LASS ZOCKEN • Indie vs HipHop • Lido Berlin", "Sat, Apr 22, 2023 23:59 (CEST)", "Berlin"])

# print("---------sommerpass.csv---------\nEvent title / Date / City")
# with open('sommerpass.csv', newline='') as csvfile:
#     file = csv.reader(csvfile, delimiter=',', quotechar='"')
#     next(file) # skip header
#     for row in file:
#         print(', '.join(row))
# print("------------------------------")

# # TASK 6
# while True:
#     if(os.stat("gym.csv").st_size == 0):
#         with open('gym.csv', 'w', newline='') as csvfile:
#             file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             file.writerow(["Age", "First name", "Surname", "Pass exp. date"])
#     print("Option 1: Add a member to the database.\nOption 2: List all members in the database.\nOption 3: Exit.")
#     userChoise = int(input("Choose your action: "))
#     if(userChoise == 1):
#         newMemberData = []
#         for i in range(0, 4):
#             if(i == 0):
#                 line = "first name"
#             elif(i == 1):
#                 line = "surname"
#             elif(i == 2):
#                 line = "age"
#             if(i == 3):
#                 line = "pass exp. date"
#             newMemberData.append(input("Enter members %s: "  % (line)))
#         with open('gym.csv', 'a', newline='') as csvfile:
#             file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             file.writerow([newMemberData[0], newMemberData[1], newMemberData[2], newMemberData[3]])
#     elif(userChoise == 2):
#         print("---------gym.csv---------\nAge / First name / Surname / Pass exp. date")
#         with open('gym.csv', newline='') as csvfile:
#             file = csv.reader(csvfile, delimiter=',', quotechar='"')
#             next(file) # skip header
#             for row in file:
#                 print(', '.join(row))
#         print("------------------------------")
#     elif(userChoise == 3):
#         print("Bye!")
#         break
#     else:
#         print("Error!")