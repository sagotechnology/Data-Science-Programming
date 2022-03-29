''' https://gist.github.com/joaofeitoza13/e8b604181f29f386e2271be59d58ac1e '''


from random import shuffle
from timeit import timeit
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(1000000)

def reverseArray(lenght):
	a = []
	for i in range(lenght):
		a.append(lenght-i)
	return a

def randomArray(lenght):
	a = []
	a = reverseArray(lenght)
	shuffle(a)
	return a

def quickSort(array):
	pivote = len(array) // 2
	lesser, equal, greater = [], [], []
	for i in range(len(array)):
		if array[i] < array[pivote]: 
			lesser.append(array[i])
		elif array[i] > array[pivote]: 
			greater.append(array[i])
		else: equal.append(array[i])
	if len(lesser) > 1: 
		lesser = quickSort(lesser)
	if len(greater) > 1:
		greater = quickSort(greater)
	return lesser + equal + greater

def quickSortW(alist):
	quickSortWHelper(alist,0,len(alist)-1)

def quickSortWHelper(alist,first,last):
	if first<last:
		splitpoint = partition(alist,first,last)
		quickSortWHelper(alist,first,splitpoint-1)
		quickSortWHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
	pivotvalue = alist[first]
	leftmark = first+1
	rightmark = last
	done = False
	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1
		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1
		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp
	return rightmark

timeRandom = []
timeReverse = []
timeWorse = []
timeBigger = []
lenght = []
lenghtBigger = []
elements = [1000, 2000, 3000, 4000, 5000, 7000]
elementsBigger = [50000, 100000, 200000, 400000, 800000, 1000000]

def desenhaGrafico(xl = "Qnt. Elements(und)", yl = "Time(sec)"):
	
	plt.subplot(211)
	plt.title('Quicksort Analysis', fontsize=20)
	plt.plot(lenght, timeRandom, label = "Quicksort - Random")
	plt.plot(lenght, timeReverse, label = "Quicksort - Reversed")
	plt.plot(lenght, timeWorse, label = "Quicksort - Worse")
	legend = plt.legend(loc='upper left', shadow=True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')

	plt.subplot(212)
	plt.plot(lenghtBigger, timeBigger, label = "Quicksort - Bigger")
	legend = plt.legend(loc='upper left', shadow=True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')
	
	plt.xlabel(xl)
	plt.ylabel(yl)
	plt.show()	
	
def main():
	for _tmp in elements:
		lenght.append(_tmp)
		arrayRandom = randomArray(_tmp)
		arrayReverse = reverseArray(_tmp)
		arrayWorse = reverseArray(_tmp)
		timeRandom.append(timeit("quickSort({})".format(arrayRandom), 
			setup = "from __main__ import quickSort", number = 1))
		timeReverse.append(timeit("quickSort({})".format(arrayReverse), 
			setup = "from __main__ import quickSort", number = 1))
		timeWorse.append(timeit("quickSortW({})".format(arrayWorse),  
			setup = "from __main__ import quickSortW", number = 1))
	for _tmp in elementsBigger:
		lenghtBigger.append(_tmp)
		arrayBigger = reverseArray(_tmp)
		timeBigger.append(timeit("quickSort({})".format(arrayBigger), 
			setup= "from __main__ import quickSort", number = 1))
		
	desenhaGrafico()

if __name__ == "__main__":
	main()