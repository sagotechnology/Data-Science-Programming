price = round(float(input("Enter the price of a meal: $")),2)

tip = round(price * 0.16, 2)
total = round(price + tip, 2)

print("A 16% tip would be $" + "{:.2f}".format(tip))
print("The total including tip would be $" + "{:.2f}".format(total))