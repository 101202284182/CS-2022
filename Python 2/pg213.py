#TASK 1
def search(array, numToSearch):
    for i in range(0, len(array)):
        if(array[i] == numToSearch): return True
        return False

array = [19, 87, 1, -1, 11, 0, 4, 33, 19]
print(search(array, -1))