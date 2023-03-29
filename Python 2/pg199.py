#TASK 1
# def printHB():
#     print("Happy Birthday!")

# for i in range (0,3):
#     printHB()

#TASK 2
# def calcPi():
#     print(22/7)

# calcPi()

#TASK 3
# numberA = int(input("Enter number A: "))
# numberB = int(input("Enter number B: "))

def mult(a, b):
    print(a * b)

# mult(numberA, numberB)

#TASK 4
# baseNum = int(input("Enter base number: "))
# indexNum = int(input("Enter index number: "))

def calcPower(a, b):
    print(a**b)

# calcPower(baseNum, indexNum)

#TASK 5
# numberA = int(input("Enter number A: "))
# numberB = int(input("Enter number B: "))

# def findBigger(a, b):
#     if(a > b):
#         return a
#     return b

# print(findBigger(numberA, numberB))

#TASK 6
# depth = int(input("Enter depth: "))
# width = int(input("Enter width: "))
# length = int(input("Enter length: "))

# def calcVolume(a, b, c): # a - length, b - width, c - depth
#     print(a * b * c)

# calcVolume(length, width, depth)

#TASK 7
# stringA = str(input("Enter string A: "))
# stringB = str(input("Enter string B: "))

# def stringCheck(a, b):
#     if(a == b):
#         print("They are identical!")
#         return
#     print("They are not identical!")

# stringCheck(stringA, stringB)

#TASK 8
# userEmail = str(input("Enter your email: "))

def checkEmail(email):
    if(email.find("@") == -1 or email.find(".") == -1 or len(email) < 8):
        return False
    return True

# if(checkEmail(userEmail) == True):
#     print("Email is ok!")
# else: 
#     print("Error!")

#TASK 9
# userString = str(input("Enter your string: "))
# userChara = str(input("Enter your character: "))

# def findChara(string, chara):
#     charaCount = 0
#     for i in range(0, len(string)):
#         if(string[i] == chara):
#             charaCount += 1
#     return charaCount

# print(findChara(userString, userChara))

#TASK 10
checkEmail("me@vo1ter.me")
mult(2, 2)
calcPower(2, 2)