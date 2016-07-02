input_id = input("Enter your ID.\n")
input_pwd = input("Enter your password.\n")
real_id = "egoing"
real_pwd = "11"
if real_id == input_id:
    if real_pwd == input_pwd:
        print("Hello")
    else:
        print("you put the wrong password")
else:
    print("You put the wrong ID")
