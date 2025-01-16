# Basic Calculator
while (True):
    # taking input from the user
    print("Enter two numbers(Enter 0 0 to exit): ")
    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))

    if (num1 == 0 and num2 == 0):
        print("\n...Exit...")
        break

    # performing the operation
    operator = input("Enter an operator: \n")
    if operator == "+":
        print(f"{num1} + {num2} = {num1 + num2}")

    elif operator == "-":
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operator == "*":
        print(f"{num1} * {num2} = {num1 * num2}")

    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed!")
            continue
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operator")
