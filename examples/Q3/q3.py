num1=float(input("enter your number1: "))  
operator=input("print your operator: ")
num2=float(input("enter your number2: "))
if operator=='sum':
    print(num1+num2)
elif operator=='difference':
    print(num1-num2)
elif operator=='multiple':
    print(num1*num2)
elif operator=='divide':
    print(num1/num2)