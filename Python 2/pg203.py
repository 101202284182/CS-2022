from random import randint
#TASK 1
# def calcPi():
#     return 22/7

# print(calcPi())

#TASK 2
# def divide(num1, num2):
#     return num1 / num2

# print(divide(randint(1, 64000), randint(1, 64000)))

#TASK 3
# def countSpaces(string):
#     string = string.split(" ")
#     return len(string)

# print(countSpaces("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id ex a nulla mollis maximus eu in justo. Duis non cursus est. Nam arcu urna, consectetur quis ultrices vitae, ultrices nec eros. Donec vitae finibus leo. Vestibulum rutrum facilisis nisl eget laoreet. Sed iaculis, risus suscipit cursus iaculis, dui nunc sodales nunc, in luctus orci lacus varius mi. Sed luctus ullamcorper enim, vitae egestas nulla cursus ut. Donec vel justo vehicula justo ornare elementum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus molestie lectus lacinia feugiat vestibulum."))

#TASK 4
# def checkNum(num1, num2):
#     if(num1 == num2):
#         return True
#     return False

# print(checkNum(0 ,0))
# print(checkNum(1, 0))

#TASK 5
# def countAppears(list, whatToFind):
#     counter = 0
#     for item in range(len(list)):
#         if(item == whatToFind):
#             counter += 1
#     return counter

# randomList = []
# i = 0
# while i < 64:
#     randomList.append(randint(0, 128))
#     i += 1

# print(countAppears(randomList, randint(0, 128)))

#TASK 6
# def salePriceCalc(rrp, discount):
#     return (rrp - discount) * rrp

# i = 0
# while i < 6:
#     print(salePriceCalc(randint(201, 500), randint(1, 200)))
#     i += 1

#TASK 7
# def tempConvert(temp, convertTo):
#     convertTo = convertTo.upper()
#     temp = int(temp)
#     if(convertTo == "F"):
#         return (temp - 32) * 0.5666
#     elif(convertTo == "C"):
#         return (temp - 32) * 0.5666
#     else:
#         return "Error"

# print(tempConvert(50, "f"))
# print(tempConvert(102, "C"))
# print(tempConvert(37, "F"))
# print(tempConvert(20, "C"))

#TASK 8
# def foodCalc(animal, foodG):
#     if(animal.lower() == "cat"):
#         return (foodG / 1000) * 5
#     if(animal.lower() == "hamster"):
#         return (foodG / 1000) * 3
#     else:
#         return "Error"

# userAnimal = str(input("Enter your animal: "))
# userFoodG = int(input("Enter amount of food in gramms: "))

# print(foodCalc(userAnimal, userFoodG))