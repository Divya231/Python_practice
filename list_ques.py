l=[3,4,5,6]
print(l)
# using negative index
print(l[-1])
# positive index
print(l[len(l)-1])

# if i want to check 7 is present in list or not
if 7 in l:
    print("Yes")
else:
    print("No")

# If i want to check for string 
    
if "vya" in "Divya":
    print("Yes , vya is resent in string")

print(l[-1::-1])
print(l[1:])
print(l[-1:])
print(l[1::2])