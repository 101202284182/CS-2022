import csv
#TASK 1
# name = input("Enter your name: ")
# file = open("pg77_1.txt", "w")
# file.write(name)
# file.close

#TASK3
# userInput = input("Enter password: ")
# file = open("pg77_2.txt", "r")
# password = file.read()
# file.close

# if password == userInput: 
#     print("Correct")
# else:
#     print("Error")

#TASK 4
# userNums = []
# i = 0
# while i < 10:
#     userNums.append(int(input("Enter %d number: " % (i+1))))
#     i +=1
    
# with open('pg77_4.csv', mode='w', newline='') as file:
#     file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     file.writerow(userNums)

#TASK 5
with open('pg77_4.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    i = 0
    arr = []
    for row in reader:
        while i < 10:
            arr.append(float(row[i]))
            i +=1
    print(arr)

#TASK 6
salesPeople = []
sales = []

while True:
    name = str(input("Type your name: "))
    if(name in salesPeople):
        print("You are already in the system!")
        continue
    salesInput = float(input("Type value of your total sales: "))

    salesPeople.append(name)
    sales.append(salesInput)
    with open('pg77_6_1.csv', mode='w', newline='') as file:
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(salesPeople)
    with open('pg77_6_2.csv', mode='w', newline='') as file:
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(sales)

    a = str(input("Add another one salesperson? (y/n): "))
    if(a.lower() == "y"):
        continue
    else:
        break

print("----------- PERSONAL STATS -----------")
for i in range(0, len(salesPeople)):
    print("%s - %d€ sold" % (salesPeople[i], sales[i]))