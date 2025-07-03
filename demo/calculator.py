num_One =int(input("enter a number: "))
num_two =int(input("enter a number: "))

add= num_One+num_two
sub= num_One-num_two
mul= num_One*num_two
div= num_One/num_two
while True:
    user_option=str(input("select a option:+,-,*,/: "))
    if user_option== "exit":
        break
    if user_option=="+" :
        print(add)
    elif user_option=="-" :
        print(sub)
    elif user_option=="*" :
        print(mul)
    elif user_option=="/" :
        print(div)
    else:
        print("invalid")

