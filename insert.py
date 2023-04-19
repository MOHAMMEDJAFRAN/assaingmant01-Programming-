from authontication import *

file = open("student.txt", "a")

user_Name = input("Enter Your Username :  ")
passWord = input("Enter Your Password :  ")
files = "login.txt"

# txt file data to compare username and password

if (signin(user_Name, passWord, files) == True):
    while True:
        print("\t\t\t\t\t\t", '\033[4m', '\033[1m', "STUDENTS DETAILS", '\033[0m', "\n")
        s_ID = input("Enter your Student ID (and type exit): ")
        if (s_ID == "exit"):
            print('\033[91m', '\033[1m', "----------You are exit------------")
            break
        else:
            s_Name = input("Enter Your Student Name: ")
            s_Age = input("Enter Your Student Age: ")
            s_Location = input("Enter Your Student Location: ")
            print(input("<<<<< PRESS ENTER >>>>>"))
            print("\t", "\t", '\033[1m', "-----------Student Details Succsesfully!-----------", "\t", "\t", "\n")
            s_details = s_ID + ":" + s_Name + ":" + s_Age + ":" + s_Location
        file.write(s_details + "\n")
else:
    print("\t", "\t", '\033[1m', "---<<<<Password Incorrect Try again!>>>>----", "\t", "\t", "\n")
