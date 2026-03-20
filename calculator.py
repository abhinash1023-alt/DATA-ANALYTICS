# ...existing code...

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("choose operation(+,-,*,/): ")
    if operation == "+":
        print("result:", num1 + num2)
    elif operation == "-":
        print("result:", num1 - num2) 
    elif operation == "*":
        print("result:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("error: division by zero!"
        else:
            print("result:", num1 / num2)
    else:
        print("Invalid operation!")
except ValueError:
    print("Error: Please enter valid numbers!")


