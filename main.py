import math
import random

# The amount of times the 4 - 2 - 1 loop is allowed to repeat before moving to the next number.
fourTwoOneCountMax = 3
# This value can be any floating point number, ideally between 0 and 2. MUST BE A FLOAT
y = 1.006
z = 0

def main():
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

def collatz(n):
	initialValue = n
	totalCount = 0
	while n != 1:
		# This is the collatz conjecture "game logic"
		# If n is an even number, divide it by 2, otherwise multiply it by 3 and add one. 
		n = n / 2 if n % 2 == 0 else n * 3 + 1
		totalCount += 1
	# This outputs the number of times the collatz conjecture was run before hitting a [4, 2, 1, 4]loop. 
	print (f"The number '{round(initialValue, 6)}' returned 4,2,1 in {totalCount} iterations.")

main()
