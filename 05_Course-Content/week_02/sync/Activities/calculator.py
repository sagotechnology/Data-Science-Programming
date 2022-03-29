a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    calc = a + b
elif operator == "-":
    calc = a - b
elif operator == "*":
    calc = a * b
elif operator == "/":
    calc = a / b
else:
    calc = "invalid"

if calc == "invalid":
    print("Invalid operator")
else:
    print(a, operator, b, "=", calc)
