def signin(user_Name, passWord, file):
    myfile = open(file, "r")
    user = []
    pword = []
    for line in myfile:
        value = line.strip().split(",")
        user.append(value[0])
        pword.append(value[1])

    for i in range(len(user)):
        if user_Name == user[i] and passWord == pword[i]:
            return True
            break
    else:
        return False
