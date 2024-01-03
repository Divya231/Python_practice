s1="Learing python is {}".format("easy")
s2="Learning Machine Learning is {}".format("interesting")
print(s1,s2)


n="hi my name is {0} , and my age is {1}".format("divya",22)
p="hi my name is {1} , and my age is {0}".format("divya",22)
print(n ,p)
n="hi my name is {a} , and my age is {b}".format(a="divya",b=22)

print(n)
n="hi my name is {a} , and my age is {b:10}".format(a="divya",b=22)
# b:10 -------> how much length of character or integer will stored
print(n)
n="hi my name is {a} , and my age is {b:^10}".format(a="divya",b=22)
# b:^10 ---> character will come in the middle
# b:<10 ----> character will come in left
# b:>10 ---->character will come in right (default)
print(n)