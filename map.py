#  map is a built-in function that allow you to apply function to a sequence of element and returm new sequemece

def cube(x):
    return x*x*x


# print(cube(7))
# 2 method
l=[2,4,6,3,2]
# new=[]
# for item in l:
#     new.append(cube(item))
# print(new)

# 3 method
# Using map function
newl=map(cube,l)
print(newl)
newl=list(map(cube,l))
print(newl)
newl=tuple(map(cube,l))
print(newl)
newl=set(map(cube,l))
print(newl)