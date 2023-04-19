from authontication import *

# get user input
print("\t\t\t\t\t", '\033[93m', '\033[1m', "---------Login to Your Account---------", '\033[0m', "\n")
user_Name = input("Enter Your Username :  ")
passWord = input("Enter Your Password :  ")
print(input("<<<<PRESS ENTER>>>>"))

# txt file sourse asign to file
files = "login.txt"

# txt file data to compare username and password

if (signin(user_Name, passWord, files) == True):
    # username,password correct in read student.txt file

    print("\n", "\t\t\t" + '\033[95m' + '\033[1m' + '\033[4m', "------------STUDENTS DETAILS----------" + '\033[0m')
    print("\n" + '\033[4m' + "Student_ID" + "\t" + '\033[0m', '\033[4m', "Student_Name" + '\033[0m', "\t",
          '\033[4m' + "Student_Age" + '\033[0m' + "\t",
          '\033[4m' + "Students_Location" + '\033[0m' + "\n")  # '\033[4m 'underline start    # '\033[0m' =underlin end
    file = open("student.txt", "r")
    for i in file:
        line = i.strip().split(":")
        print(line[0] + "\t\t\t\t" + line[1] + "\t\t\t " + line[2] + "\t\t\t\t " + line[3])

    file = open("student.txt", "r")

    s_name = []
    s_age = []
    for line in file:
        value = line.strip().split(":")
        s_name.append(value[1])
        s_age.append(int(value[2]))
    print("\n", "No. of Students: ", "\t\t\t", len(s_name))
    print("Lowest Age of Student: ", "\t", min(s_age))
    print("Highest Age of Student: ", "\t", max(s_age))

else:
    print('\033[91m', '\033[1m', "User name,Password Incorrect!")
