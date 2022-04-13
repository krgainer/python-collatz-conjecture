import itertools
import time


def itertoolsFunction():
	for i in itertools.count(1):
		print (i)
		if i < 10000000000:
			break

def plusOneFunction():
	e = 0
	while True:
		e += 1
		print (e)
		if e < 10000000000:
			break

def main():
	start_time = time.time()
	itertoolsFunction()
	print(f"--- Itertools comepleted in: {time.time() - start_time} seconds! ---")
	start_time = time.time()
	plusOneFunction()
	print(f"--- i+=1 comepleted in: {time.time() - start_time} seconds! ---")

main()