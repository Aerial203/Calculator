def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(n1, n2, operation):
    return operation(n1, n2)


def process(num1: float, num2: float, operator: str) -> float:
    if operator == "+":
        operate = calculate(num1, num2, add)
    elif operator == "-":
        operate = calculate(num1, num2, subtract)
    elif operator == "*":
        operate = calculate(num1, num2, multiply)
    elif operator == "/":
        operate = calculate(num1, num2, divide)
    else:
        print("Wrong input")
        return False
    return operate


cal_on = True
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Operation: ")
result = process(a, b, op)
if not result:
    print("Check the operation carefully")
    cal_on = False
while cal_on:
    print(f"Result: {result}")
    if not (input("Do you want to continue: ") == ("y" or "Y")):
        print(f"Final result: {result}")
        print("Bye!")
        cal_on = False
        break
    n3 = float(input("Enter the number: "))
    op = input("Enter operation: ")
    result = process(result, n3, op)
