#TASK 1
# def calcPi():
#     return 22/7

# def unitTest():
#     answer = calcPi()
#     expectedReturn = 22/7
#     if(answer == expectedReturn): return True
#     return False

# print(unitTest())

#TASK 2
# def multiplyNumbers(num1, num2):
#     return int(num1) * int(num2)

# def unitTest():
#     fails = 0
#     testValues = [[1, 2, 3, 10, 55], [1, 2, 3, 5, 9]]
#     expectedReturns = [1, 4, 9, 50, 495]
#     for i in range(0, len(expectedReturns)):
#         answer = multiplyNumbers(testValues[0][i], testValues[1][i])
#         if(answer != expectedReturns[i]): fails += 1
#     return fails

# print(unitTest())

#TASK 3
# def checkEven(num):
#     if(isinstance(num, int) == False): return False
#     if(isinstance(num / 2, int) == True): return True

# def unitTest():
#     fails = 0
#     testValues = [1, 2, 55.5, "test", False]
#     expectedReturns = [False, True, False, False, False]
#     for i in range(0, len(expectedReturns)):
#         answer = checkEven(testValues[i])
#         if(bool(answer) != expectedReturns[i]): fails += 1
#     return fails

# print(unitTest())

#TASK 4
# def factorial(num):
#     result = 1
#     if(num < 0): return "Error"
#     if(num == 0): return result
#     for i in range(1, num + 1):
#        result = result * i
#        print(result)
#     return result

# def unitTest():
#     fails = 0
#     testValues = [1, 5, 10]
#     expectedReturns = [1, 120, 3628800]
#     for i in range(0, len(expectedReturns)):
#         answer = factorial(testValues[i])
#         if(answer != expectedReturns[i]): fails += 1
#     return fails

# print(unitTest())

#TASK 5
def maxNum(num1, num2, num3):
    nums = [num1, num2, num3]
    return max(nums)

def unitTest():
    fails = 0
    testValues = [[2, 4, 1],
                  [4, 2, 1],
                  [1, 2, 4]]
    expectedReturns = [4, 4, 4]
    for i in range(0, len(expectedReturns)):
        answer = maxNum(testValues[i][0], testValues[i][1], testValues[i][2])
        if(answer != expectedReturns[i]): fails += 1
    return fails

print(unitTest())