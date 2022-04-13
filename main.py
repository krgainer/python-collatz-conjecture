import math


fourTwoOneCountMax = 3 # The amount of times the 4 - 2 - 1 loop is allowed to repeat before moving to the next number.
z = 0


def floatNum():
	y = 1.00006 # This value can be any floating point number, ideally between 0 and 2. MUST BE A FLOAT
	x = 1
	# This checks to make sure that v times your multiplier (y) is within range of inifinty
	while x <= ( (math.inf) - (x*y) ):
		z = x
		x *= y
		if x != z:
			collatz(x)
		else:
			print ("The multiplier entered has resulted in an infinite loop.")
			break


def intNum():
	x = 0
	# This checks to make sure that v times your multiplier (y) is within range of inifinty
	while True:
		x += 1
		collatz(x)


def collatz(n):
	initialValue = n
	totalCount = 0
	nMax = 0
	while n != 1 or 0:
		# This is the collatz conjecture "game logic"
		# If n is an even number, divide it by 2, otherwise multiply it by 3 and add one. 
		n = n / 2 if n % 2 == 0 else n * 3 + 1
		totalCount += 1
		nMax = n if n > nMax else nMax
	# This outputs the number of times the collatz conjecture was run before hitting a [4, 2, 1, 4] loop. 
	print (f"The number '{round(initialValue, 6)}' returned 4,2,1 in {totalCount} iterations. The highest number reached was {nMax}.")


def main():
	intNum()


main()
