input_id = input("Enter your ID.\n")
input_pwd = input("Enter your password.\n")
real_id = "egoing"
real_pwd = "11"
if real_id == input_id and real_pwd == input_pwd:
    print("Hello")
else:
    print("You failed to sign-in. Please check your ID or Password again.\n")
