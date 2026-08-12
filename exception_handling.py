print("Simple Division")

try:
    num1 = float(input("enter num1 :"))
    num2 = float(input("enter num2 :"))
    result=num1/num2
    print("Result:",result)

except ValueError:
    print("Error:Enter valid num")

except ZeroDivisionError:
    print("Error:Cannot divisible by zero")

finally:
    print("Program execution completed")