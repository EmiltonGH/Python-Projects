def calculator():
    print("Welcome to the calculator program")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose an operation")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/")

    operation = input("Enter your choice of operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero is not allowed."
    else:
        result = "Invalid operation selected."

    print("The result is:", result)

calculator()

