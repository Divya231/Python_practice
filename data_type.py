a=10
b="divya"
c= 12.8
d=2+3j
print(type(a),type(b),type(c),type(d))

# string

S="Learning Python"
s='''Python 
     is 
easy    
     to 
learn'''
print(S)
print(s)
print(type(s),type(S))


# List


list=["Divya",100,"python","learning"]
list[1]="Machine_learning"
print(type(list))
print(list)



# Tuple


tuple=("Data-science","Machine_learning",10,45,"Python")
print(type(tuple))


# Dictionary

dic = {
    'name' : 'Divya' ,
    'Interest' : 'Python' ,
    'Profile' : 'Devops'
}
print(type(dic),dic)
print(dic['name'])

# set

set={1,2,3,1,"divya","python",45,"python"}
print(type(set),set)