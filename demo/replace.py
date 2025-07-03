lists=["apple","orange","banana","cherry","kiwi"]
new_list=[]
replaced="haloo"
for x in lists:
    if "a" in x:
        x=x.replace(x,replaced)
    new_list.append(x)
    print(new_list)




