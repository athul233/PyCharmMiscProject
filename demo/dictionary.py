this_dict={
    "username":"n",
    "password":"p"}

while True:
    input_1 = input("enter the username: ")
    input_2 = input("enter password : ")
    if input_1 == "n" and input_2 == "p":
        print("login successfully completed")
        break

    else:
        print("login failed.... please try again")
