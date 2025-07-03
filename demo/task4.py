num_one=float(input("enter the first number: "))
num_two=float(input("enter the second number: "))
num_three=float(input("enter the thrid number:"))

if (num_one>num_two) and (num_one>num_three):
    largest=num_one
elif num_two>num_one and num_two>num_three:
    largest=num_two
elif num_three>num_one and num_three>num_two:
    largest=num_three

else:
    print("invalid")
print("largest number is:", largest)
