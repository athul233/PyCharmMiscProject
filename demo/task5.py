age=int(input("enter your age "))
if age>=100:
    print("aren't you too old for voting")
elif age>=18:
    print("congratulation! your eligible for voting")
elif age<18:
    print("sorry! your not eligible")

else:
    print("invalid")