i = int(input("Enter the first number: "))
j = int(input("Enter the second number: "))

def algorithm_sequence(j):
	sequence = []
	sequence.append(j)
	k = 0
	while True:
		if sequence[k] == 1:
			break
		else:
			if sequence[k] % 2 != 0:
				n = 3*sequence[k] + 1
			else:
				n = sequence[k] / 2
			sequence.append(n)
		k = k + 1
	return sequence
n = i
cycles = []
while n <= j:
	sequence = algorithm_sequence(n)
	cycles.append(len(sequence))
	n = n + 1
print(i,j,max(cycles))
