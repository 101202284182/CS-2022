#TASK 1
# def fibonacci(start, end):
#     result = [0, 1]
#     for i in range(0, end - start):
#         result.append(result[i] + result[i + 1])
#         i += 1
#     return result
    
# print(fibonacci(1, 5))

#TASK 2
# def fibonacci(end):
#     if(len(result) >= end or end < 0): return result
#     result.append(result[len(result) - 1] + result[len(result) - 2])
#     return fibonacci(end)

# result = [0, 1]

# print(fibonacci(10))

#TASK 3
# def addUp(end):
#     if(len(result) > end or end < 0): return sum(result)
#     result.append(result[len(result) - 1] + 1)
#     return addUp(end)

# result = [0]

# print(addUp(5))