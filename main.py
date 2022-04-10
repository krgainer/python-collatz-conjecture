import math

fourTwoOneCount = 0
fourTwoOneCountMax = 3
inf = math.inf
y = 1.02

def main():
	v = 1
	while v <= (inf - (v*y)):
		v *= y
		collatz(v)

def collatz(inputVal):
	print(f"Current Input: {inputVal}")
	fuckVal = True
	fourTwoOneCount = 0
	totalCount = 0
	while fuckVal:
		inputVal = inputVal / 2 if inputVal % 2 == 0 else inputVal * 3 + 1
		if inputVal == 4 and fourTwoOneCount <= fourTwoOneCountMax:
			fourTwoOneCount += 1
			print (fourTwoOneCount)
		if fourTwoOneCount == fourTwoOneCountMax+1:
			fuckVal = False
		else:
			totalCount += 1

	print (f"Fuck caught at: {totalCount}")

main()
