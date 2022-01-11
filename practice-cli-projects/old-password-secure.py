secure = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '!'), ('l', '|'))

def convert(password):
    for a,b in secure:
        password = password.replace(a , b)
    return password

if __name__ == "__main__":
    oldpassword = input("Enter your password : ")
    # newpassword = convert(oldpassword.lower())
    newpassword = convert(oldpassword)
    print(f"Your secure password is : {newpassword}")