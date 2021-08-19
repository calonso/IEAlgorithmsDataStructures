
def mastermind(min, max, value):
	middle = round((max - min) / 2)
	attempts = 1
	while middle != value:
		print(f'{min} to {max} using {middle}')
		attempts += 1
		if middle > value:
			max = middle
		else:
			min = middle
		middle = round(min + ((max - min) / 2))
	return attempts


print(mastermind(0, 100, 50))
print(mastermind(0, 100, 51))
print(mastermind(0, 100, 0))
print(mastermind(0, 100, 100))