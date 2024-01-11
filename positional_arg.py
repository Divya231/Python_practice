def pos_arg(name,age):
    print("Hello",name,"and age is : ", age)

name=input("Enter name: ")
age=int(input("Enter age: "))
pos_arg(name,age)
# wrong position
pos_arg(age,name)