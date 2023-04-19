print("\t\t\t\t  " + '\033[1m' + "---------Hello----------")  # font bold
print("\t\t\t\t" + '\033[1m' + "*****Creat your Account******")  # font bold
userName = input("Enter the username:    ")
passWord = input("Enter the password:    ")
repassWord = input("Re-Enter the password: ")
print("\t\t\t\t\t\t" + '\033[94m' + input("<-----PRESS ENTER KEY ----->"))

with open("login.txt", "r") as file:
    if (passWord == repassWord):
        for line in file:
            use, word = line.strip().split(",")
            if (userName == use and passWord == word):
                print('\033[91m', "***already include****!")  # font red color
                break
        else:
            y = open("login.txt", "a")

            y.write(userName + "," + passWord + "\n")
            print("\t\t\t\t\t", '\033[1m', "Login Succesfully Complete!")
    else:
        print('\033[91m' + "Password not Match")  # font bold
