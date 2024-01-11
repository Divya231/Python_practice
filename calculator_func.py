def calculator(n1,n2):
    if(op=='+'):
        print("Addition of two number : ",n1+n2)
    elif(op=='-'):
        print("Subtraction of two number : ",n2-n1)
    elif(op=='*'):
        print("Multiplication of two number : ",n1*n2)
    elif(op=='/'):
        print("Division of two number : ",n2/n1)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number : "))
op=input("Enter operator: ")
calculator(num1,num2)
