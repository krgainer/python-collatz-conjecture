import math

fourTwoOneCount = 0
fourTwoOneCountMax = 3
## This value can be any floating point number, ideally between 0 and 2. 
y = 1.0000084
# valed through 1.3222491729511548e+16
z = 0

def main():
	v = 1
	# This checks to make sure that v times your multiplier (y) is within range of inifinty
	while v <= ( (math.inf) - (v*y) ):
		z = v
		v *= y
		if v != z:
			collatz(v)

def collatz(inputVal):
	initialValue = inputVal
	fuckVal = True
	fourTwoOneCount = 0
	totalCount = 0
	while fuckVal:
		## This is the collatz conjecture "game logic".bool()
		## If inputVal is an even number, divide it by 2, otherwise multiply it by 3 and add one. 
		inputVal = inputVal / 2 if inputVal % 2 == 0 else inputVal * 3 + 1
		## Allows x amount of bounces of [4, 2, 1, 4], determined by fourTwoOneCountMax, to be played before moving to the next number.
		## this part is written weird, but only for furture data gathering purposes		
		if inputVal == 4 and fourTwoOneCount <= fourTwoOneCountMax:
			fourTwoOneCount += 1
		if fourTwoOneCount == fourTwoOneCountMax+1:
			fuckVal = False
		else:
			totalCount += 1
# This outputs the number of times the collatz conjecture was run before hitting a [4, 2, 1, 4] loop. 
	print (f"The number '{round(initialValue, 6)}' returned 4,2,1 in {totalCount} iterations.")

main()
