def process_order(x_list):
    x = x_list.pop()
    print("You filled an order for", x[1], x[0], "for a total of", \
          "${:.2f}".format(x[2] * x[1]))
    global total
    total += round(x[2] * x[1], 2)

total = 0

x = [("oranges", 4, 3.22),("gummy bears",1,1.99),("sour bites", 3, 2.33), ("antacid", 1, 5.33)]
while(len(x)>0):
    process_order(x)
print("Total price: ${:.2f}".format(total))