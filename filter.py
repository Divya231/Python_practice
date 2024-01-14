def filter_function(a):
    return a>1

l=[1,2,4,8,6,3,2,5,9]
new=filter(filter_function,l)
print(new)

l=[1,2,4,8,6,3,2,5,9]
new=list(filter(filter_function,l))
print(new)

l=[1,2,4,8,6,3,2,5,9]
new=tuple(filter(filter_function,l))
print(new)

l=[1,2,4,8,6,3,2,5,9]
new=set(filter(filter_function,l))
print(new)