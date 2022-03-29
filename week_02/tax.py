income = round(float(input("Please enter your income: $")), 2)
#
# if income is less than or equal $1000.00
if income <= 1000:
    tax = round(income * 0.05, 2)
# if income is greater than $1000.00 but less than or equal to $2000.00 
elif 1000 < income <= 2000:
    tax = round(50 + (income - 1000) * 0.10, 2)
# if income is greater than $2000.00
else:
    tax = round(50 + 100 + (income - 2000) * 0.15, 2)
print("\nThe tax you owe is:","${:.2f}".format(tax))