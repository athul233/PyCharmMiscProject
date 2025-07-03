lis=[1,3,5,7,8,9,12,10,14]
odd_lis=[]
even_lis=[]
for i in lis:
    if i%2==0:
        even_lis.append(i)
    else:
        odd_lis.append(i)
print(f"Odd:{odd_lis}")
print(f"even:{even_lis}")


