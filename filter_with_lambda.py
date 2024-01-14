l=[1,2,4,5,2,3,4]
new=list(filter(lambda a:a>2, l))
print(new)
new=tuple(filter(lambda a:a>2, l))
print(new)
new=set(filter(lambda a:a>2, l))
print(new)