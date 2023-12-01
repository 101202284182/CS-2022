#TASK 1
def search(array, numToSearch):
    for i in range(0, len(array)):
        if(array[i] == numToSearch): return True
        return False

array = [19, 87, 1, -1, 11, 0, 4, 33, 19]
print(search(array, -1))

#TASK 4
#SUBTASK A
def search(arr, num):
    result = False
    for i in range(0, len(arr)):
        if(arr[i] == num):
            result = True
            return result
    if(result == False):
        return result
     
toSearch = [19, 87, 1, -1, 0, 11, -1, 33, 19]
print(search(toSearch,-1))
print(search(toSearch,33))
print(search(toSearch,117))

#SUBTASK B
def search(arr, num):
    result = False
    for i in range(0, len(arr)):
        if(arr[i] == num):
            result = True
            return i
    if(result == False):
        return result
  
print(search(toSearch,-1))
print(search(toSearch,33))
print(search(toSearch,117))

#SUBTASK C
def search(arr, num):
    result = False
    for i in range(0, len(arr)):
        if(arr[i] == num):
            result = True
            return i
    if(result == False):
        return -1
  
print(search(toSearch,-1))
print(search(toSearch,33))
print(search(toSearch,117))

#SUBTASK D
def binarySearch(arr, num):
    arr.sort()
    first = 0
    last = len(arr) - 1
    while((last - first) >= 0):
        middle = first + ((last - first) // 2)
        if(arr[middle] == num):
            return middle
        elif(num < arr[middle]):
            last = middle - 1
        else:
            first = middle + 1
    return 1

print(binarySearch(toSearch, -1))
print(binarySearch(toSearch, 33))
print(binarySearch(toSearch, 117))