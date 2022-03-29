# basics of input, range checking, if and functions.

def messagesToTheEnduser(s):
	msg = "\n Update/Status message: " + s + "\n"
	print(msg)
	
def userOptions():
	print("\n Welcome.  Please choose:")
	print("\t 1 = Say hello")
	print("\t 2 = Say bonjour")
	print("\t 3 = Say buenas días")
	i = int(input("Please enter your choice:  "))
	
	if (i in range(1,4)):
		# that means the end-user entered a legit option
		if (i == 1):
			print("\n H E L L O! \n")
		elif (i == 2):
			print("\n B O N J O U R! \n")
		else:
			print("\n B U E N A S   D I A S  \n")
	else:
		messagesToTheEnduser("Sorry, that is not an option.")


userOptions()