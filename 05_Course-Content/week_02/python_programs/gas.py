gallon = float(input("Enter the amount of gasoline in gallons: "))
#
# Convert gallon to liter
liter = round(3.7854 * gallon, 4)
if gallon == 1:
    print(gallon, "gallon is equivalent to", "{:.4f}".format(liter),
          "liters.")
elif liter == 1:
    print(gallon, "gallons are equivalent to", "{:.4f}".format(liter),
          "liter.")
else: 
    print(gallon, "gallons are equivalent to", "{:.4f}".format(liter),
          "liters.")
#
# Convert gallon to barrel
barrel = round(gallon / 19.5, 3)
if barrel == 1:
   print("{:.3f}".format(barrel), "barrel of oil is used to make", gallon, 
      "gallons of gasoline")
elif gallon == 1:
    print("{:.3f}".format(barrel), "barrels of oil are used to make", gallon, 
      "gallon of gasoline")
else:
    print("{:.3f}".format(barrel), "barrels of oil are used to make", gallon, 
      "gallons of gasoline")
#
# Convert gallon to dollar
dollar = round(3.65 * gallon, 2)
if gallon == 1:
    print(gallon, "gallon of gasoline will cost", "${:.2f}".format(dollar))
else:
    print(gallon, "gallons of gasoline will cost", "${:.2f}".format(dollar))