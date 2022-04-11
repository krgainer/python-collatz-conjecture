import math
import random

# The amount of times the 4 - 2 - 1 loop is allowed to repeat before moving to the next number.
fourTwoOneCountMax = 3
# This value can be any floating point number, ideally between 0 and 2. MUST BE A FLOAT
y = 1.0000006
# validateded through 1.3222491729511548e+16
z = 0

def main():
	v = 1
	# This checks to make sure that v times your multiplier (y) is within range of inifinty
	while v <= ( (math.inf) - (v*y) ):
		z = v
		v *= y
		if v != z:
			collatz(v)
		else:
			print ("The multiplier entered has resulted in an infinite loop.")
			break

def collatz(inputVal):
	initialValue = inputVal
	fourTwoOneCount = 0
	totalCount = 0
	while True:
		# This is the collatz conjecture "game logic"
		# If inputVal is an even number, divide it by 2, otherwise multiply it by 3 and add one. 
		inputVal = inputVal / 2 if inputVal % 2 == 0 else inputVal * 3 + 1
		# Allows x amount of bounces of [4, 2, 1, 4], determined by fourTwoOneCountMax, to be played before moving to the next number.
		if inputVal == 4:
			fourTwoOneCount += 1
			if fourTwoOneCount == fourTwoOneCountMax:
				# Loop breaks once the amount of bounces of [4, 2, 1, 4] is reached.
				break
		else:
			totalCount += 1
	# This outputs the number of times the collatz conjecture was run before hitting a [4, 2, 1, 4]loop. 
	print (f"The number '{round(initialValue, 6)}' returned 4,2,1 in {totalCount} iterations.")

main()
