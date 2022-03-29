import sys
from collections import Counter, defaultdict
from colorama import Fore, Back, Style

import re
import string

''' ABOUT THIS SCRIPT: 
1) notice the libraries being imported.  Libraries are either
part of the "standard distribution" or must be installed 
separately (such as the colorama library)
2) notice the "Fore, Back, Style": these are "constants" - they are 
uneditable variables from the imported library.  The idea is that 
our own code doesn't need to be updated; while the source code itself 
can be improved and updated by the developer."
3) The Hard Way - when learning how to code we do if, for, while, comprehensions, 
lambda and other cool techniques.  Almost always there's a 3rd party library 
that can do the job faster.  In this case there's the "Counter" library - this 
is important 'cause one of the first things we do with big data is to 
(a) classify and (b) cluster the data so they're more manageable and comprehensible.
'''

def checkInput():
	# 1) ERROR CORRECTION ON INPUT - don't process 'til ready
	# 2) argument vectors ... passing data to the OS, which in turn passes them
	# to the script.  argv[0] is the name of the script; [1] is the file to read.
	# We're passing vectors to the OS to start the PYTHON INTERPRETER ... 
	# This script wants a file name - hence sys.argv[1]
	# 3) Notice the "Exceptions" - most common IndexError
	# 4) communicate with the end-user thru a single function (sendMsg) ... 
	#    and similarly we'll store error messages to our stderr.
	print("_"*60)
	try:
		sys.argv[1]
	except NameError:
		sendMsg(Back.RED + "Name isn't correctly formed .What file to parse? " + Style.RESET_ALL)
	except IndexError:
		sendMsg(Fore.RED + "IndexError: Index out of range - no arg[1].  What file to parse? " + Style.RESET_ALL)
	else:
		msgLine = Fore.WHITE + "Welcome:\n" + Fore.BLUE + "You're running script " + Fore.GREEN + sys.argv[0] + \
		" \n\twith arg vector 1 (file name to parse) = "+sys.argv[1] + Fore.BLUE

		sendMsg(msgLine)		# call this first (3) and then come back and do next function
		loadDataAndCount()		# count the data
		cleanUp()				# make sure everything is closed and say bye!

def sendMsg(s):
	print("\n\n" + "_"*60)
	print(s)
	print("_"*60 )

def cleanUp():
	sendMsg(Fore.WHITE+"\n\n Terms have been counted.\n\n"+Style.RESET_ALL)

def loadDataAndCount():
	#document_text = open("demoTextForParsing.txt", "r")
	document_text = open(sys.argv[1], "r")
	wordlist = document_text.read().lower()

	match_pattern = re.findall(r'\b[a-z]{3,15}\b', wordlist)

	# invert a temporary Counter(wordlist) dictionary so keys are
	# frequency of occurrence and values are lists the words encountered
	freqword = defaultdict(list)  # swap wordlist for match_pattern
	for word, freq in Counter(match_pattern).items():
		freqword[freq].append(word)

	# print in order of occurrence (with sorted list of words)
	for freq in sorted(freqword):
		print("count {}: {}\n".format(freq, sorted(freqword[freq])))

def main():
	# 2) "MAIN" is always the "front door" to a program
	checkInput()

# main function calling
# 1) THIS IS WHERE THE OPERATING SYSTEM TALKS TO PYTHON
if __name__=="__main__":
	main()
