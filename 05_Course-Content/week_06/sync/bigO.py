import time
import datetime
# a python test of Big O calculations for Week 6

n = 100
cnt = 0

# Q1 - compute the tightest Big ) running time bound of the following...
def timer(start):
	print("\tTime for this process: ",(time.time()-start))
	print("\tn = ", n)

def banner(s):
	print("-"*70)
	print(s)
	print("-"*70)

def q1():
	banner("Question 1 - 2 for-i in range; j in range")
	start = time.time()
	for i in range(n):
		for j in range(n^2):
			x = i + j  #print(i + j)
	timer(start)
	print("\t i iterations = ",i)

def q2():
	banner("Question 2 - while j < i")
	i = n
	j = 1
	start = time.time()
	while j < i:
		i *= 100
		j *= 101
		# print("\t", i + j)

	timer(start)
	print("\t j iterations = ",j)

def q3():
	banner("Question 3 - while and for")
	i = 0
	j = 1
	start = time.time()
	while i < n:
		for k in range(j):
			i += 1
		j *= 2
	timer(start)
	print("\t i iterations = ",i)

def q4(i):
	start = time.time()
	cnt = 0
	if i < 1:
		cnt += 1
		return 1
	else:
		cnt += 1
		return q4(i-1) + q4(i-1)
	print(q4(n))
	timer(start)
	print("\ncount [constant] ", cnt)

banner("Starting Big-O tests")
q1()
q2()
q3()
q4(n)

banner("All Done.")
