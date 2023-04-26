from firebase import firebase
myDB = firebase.FirebaseApplication("https://cs-2022-2074a-default-rtdb.europe-west1.firebasedatabase.app/", None)

# # TASK 1
# for i in range(0, 3):
#     if(i == 0):
#         record = {
#             "Make": "Honda",
#             "Model": "Civic",
#             "Reg": "191-D-1234",
#         }
#     elif(i == 1):
#         record = {
#             "Make": "Nissan",
#             "Model": "Pulsar",
#             "Reg": "182-KE-33456",
#         }
#     elif(i == 2):
#         record = {
#             "Make": "Audi",
#             "Model": "R8",
#             "Reg": "201-C-5607",
#         }
#     myDB.post("pg254/cars/", record)

# # TASK 2    
# record = {
#     "Make": "Mazda",
#     "Model": "Miata",
#     "Reg": "054-OT-99483",
# }

# myDB.post("pg254/cars/", record)

# # TASK 3
# userData = []
# for i in range(0, 3):
#     if(i == 0):
#         userData.append(input("Enter car manufacter name: "))
#     elif(i == 1):
#         userData.append(input("Enter car model: "))
#     elif(i == 2):
#         userData.append(input("Enter the license plate: "))
    
# record = {
#     "Make": userData[0],
#     "Model": userData[1],
#     "Reg": userData[2],
# }

# myDB.post("pg254/cars/", record)

# # TASK 4
# database = myDB.get("pg254/cars/", None)
# print("---------firebase/pg254/cars/---------\nMake / Model / Reg")
# for key in database:
#     print(database[key]["Make"] + " " + database[key]["Model"] + " " + database[key]["Reg"])
# print("--------------------------------------")

# # TASK 6
# userInput = []
# userCurrentFilm = []

# while len(userInput) < 5:
#     for i in range(0, 5):
#         if(i == 1):
#             userCurrentFilm.append(input("Enter film name: "))
#         elif(i == 2):
#             userCurrentFilm.append(input("Enter film director: "))
#         elif(i == 3):
#             status = 0
#             while status == 0:
#                 userFilmScore = int(input("Enter your film rating (from 1 to 10): "))
#                 if(userFilmScore < 0 or userFilmScore > 10):
#                     print("Error!")
#                 else:
#                     userCurrentFilm.append(userFilmScore)
#                     status = 1
#         elif(i == 4):
#             userInput.append(userCurrentFilm)
#             userCurrentFilm = []
#             continue

# for i in range(0, 5):
#     record = {
#         "Name": userInput[i],
#         "Director": userInput[i],
#         "Rating": userInput[i],
#     }

#     myDB.post("pg254/films/", record)