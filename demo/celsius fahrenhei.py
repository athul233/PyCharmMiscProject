while True:
    def fahrenheit():
        f =n*(9/5)+32
        print(f)
    def celsius():
        c =(n-32)*(5/9)
        print(c)
    n=int(input("enter a number :"))
    option=int(input("select one :\n1).fahrenheit to celsius converter.\n2).celsius to fahrenheit converter.\n0).Exit\n"))
    if option == 1:
        fahrenheit()
    elif option==2:
        celsius()
    else:
        print("Exit....")
        break

