password = input("Enter your password: ")

f = open("q3.txt", "r")
if(f.read() == password):
    print("Correct!")
else:
    print("Error! check your password!")