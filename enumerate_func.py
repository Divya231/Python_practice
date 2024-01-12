# Enumerate is a function in python allows you to iterate over sequence [list,tuple,string ]
# and get index number and value of each element at same time

marks=[100,34,23,98,70]
for index , mark in enumerate(marks,start=3):
    print(index,mark)
    if (index==6):
        print(index,"Awesome")
   