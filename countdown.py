
def iterative_countdown(value):
	for i in range(value, 0, -1):
		print(i)
	print('Boom!')

iterative_countdown(10)

def recusive_countdown(value):
	if value == 0:
		print('Boom!')
	else:
		print(value)
		recusive_countdown(value - 1)

recusive_countdown(1000)