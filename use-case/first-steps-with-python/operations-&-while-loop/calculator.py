while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("You cannot divide by zero!")
            continue
    else:
        print("Invalid operator!")
        continue

    print("Result:", result)

    choice = input("Do you want to continue? (T/N): ")
    if choice.upper() != "T":
        break