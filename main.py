import math

fourTwoOneCount = 0
inf = math.inf
y = 1.02

def main():
	v = 1
	while v <= (inf - (v*y)):
		v *= y
		collatz(v)

def collatz(inputVal):
	print(f"Fuck: {inputVal}")
	fuckVal = True
	fourTwoOneCount = 0
	totalCount = 0
	while fuckVal:
		inputVal = inputVal / 2 if inputVal % 2 == 0 else inputVal * 3 + 1
		if inputVal == 4 and fourTwoOneCount <= 3:
			fourTwoOneCount += 1
			if fourTwoOneCount == 4:
				fuckVal = False
			print (fourTwoOneCount)
		totalCount += 1
	print (totalCount)

main()
