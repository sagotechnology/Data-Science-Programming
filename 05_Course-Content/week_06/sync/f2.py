''' Julius Caeser's Encryption see https://en.wikipedia.org/wiki/Caesar_cipher '''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Encrypt:
	sourceAlphabet = ('abcdefghijklmnopqrstuvwxyz0123456789')
	targetAlphabet = ('XYZABCDEFGHIJKLMNOPQRSTUVW9876543210')

	def __init__(self, sourceString, encryptionType):
		self.sourceString = sourceString
		self.encryptionType = encryptionType
		
	def get_source(self):
		return self.sourceString

	def encrypterOne(self):
	
		if self.encryptionType == "A":
			print("\n\nUsing Caesar's basic letter substitution, your source string is " + bcolors.HEADER, self.sourceString + bcolors.ENDC)
			newList = []
			for i in self.sourceString:
				j = self.sourceAlphabet.index(i)
				newList.append(self.targetAlphabet[j])
			return ''.join(newList)
	

class getData:
	def start(self):
		allDone = False
		cnt = 0
		while not allDone:
			try:
				print(bcolors.BOLD + "Welcome:\nEnter your input string and choose the encryption by letter: 	" + bcolors.ENDC)
				cnt += 1
				inputL = str(input("The string to encrypt: "))
				print("Encryption choices:")
				print("\tEnter 'A' for the basic is Julius Caesar's letter substitution.")
				print("\tEnter 'B' for binary conversion.")
				print("\tEnter 'Q' to quit.  (don't use the quotes)")
				print("After 3 unsuccessful attempts, you will be logged out.")
				inputC = input("Option: ").upper()
				assert inputC in ("ABQ")
				if inputC == "Q" or cnt == 3:
					sys.exit()
				if inputC in ("AB"):
					allDone = True
			except KeyboardInterrupt:
				print(bcolors.WARNING + "You cancelled the operation." + bcolors.ENDC)
				allDone = True
				sys.exit()
			except AssertionError as error:
				print("No, no, no!  Only A, B, or Q: ", error)
		
		jce = Encrypt(inputL, inputC)
		print('And your new secret text is :' + bcolors.OKBLUE, jce.encrypterOne()  + bcolors.ENDC,  "\n\n")
	

if __name__=="__main__":
	gd = getData().start()
