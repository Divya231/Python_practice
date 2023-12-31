number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
operator=input("enter operator: + , - , * , /")
if operator=="+":
    print("Addition of two number: ",(number1+number1))
elif operator=="-":
    print("Subtraction of two number: ",(number1-number1))
elif operator=="*":
    print("Multiplication of two number: ", number1*number2)
elif operator=="/":
    print("Division of two number is:", number2/number1)
else:
    print("Error")
