# basic functions

def function_one():
	print("No parameters.")
	
def function_two(x, y):
	print("\nthis function takes 2 parameters: x and y")
	print("\tx = ",x," y = ",y)
	
def function_three(y, x = 5):
	print("\nThis puppy has 2 parameters.  One has a default value.\n")
	print("\tfirst the one without a default (y);\n\t then default for x ")
	print("\tdefault x = ",x," and y = ",y)
	
def function_four(x = 5, y = 10):
	print("\nTwo parameters with default values, note the positions...")
	print("\tthe default for x is 5, but when passed \n\ta value x = ",x, " No y as argument, so default y = ",y)
	
print("_"*60)
function_one()

print("_"*60)
function_two(5,2)

print("_"*60)
function_three(9)

print("_"*60)
function_four(8)
function_four(5, 23)

print("_"*60)