num1=float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

operator=input("Enter operator +,-,*,/ :").strip()

if operator == "+":
    print("Result:",num1+num2)
elif operator == "-":
    print("Result:",num1-num2)
elif operator == "*":
    print("Result:",num1*num2)
elif operator == "/":
    if num2 != 0:
        print("Result:",num1/num2)
    else:
        print("error, division by zero is not allowed")
else:
    print("Invalid operator")