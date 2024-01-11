def arbi_arg(*num):
    sum=0
    for i in num:
        sum=sum+i
        return sum/len(num)

c=arbi_arg(1,2,3)
print(c)
