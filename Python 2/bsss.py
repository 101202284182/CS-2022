vowels = ["a", "e", "i", "o", "u"]
password = input("Enter your password: ")
if(password == ""):
    password = "password1234"

def cryptPass(password):
    newpassword = password[0].upper()
    for i in range (1, len(password)):
        if(password[i] == "S" or password[i] == "s"): newpassword += "$"
        elif(password[i] >= 1 or password[i] <= 4): newpassword += password[i] * 2
        try:
            vowels.index(password[i])
        except:
            