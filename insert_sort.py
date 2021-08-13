
def insert_sort(data):
	for unsorted in range(1, len(data)):
		candidate = data[unsorted]
		# print(f'candidate is {candidate}')
		new_location = unsorted
		for sorted in range(unsorted, 0, -1):
			possible_index = sorted - 1
			# print(f'{candidate} vs {data[possible_index]} at {possible_index}')
			if candidate < data[possible_index]:
				new_location = possible_index
				data[sorted] = data[possible_index]
				# print(f'swap {data}')
			else:
				break
		data[new_location] = candidate
		# print(f'candidate is placed {data}')
	return data


print(insert_sort([1, 3, 2]))
print(insert_sort([1, 2, 3]))
print(insert_sort([3, 2, 1]))
print(insert_sort([1, 2, 1]))
print(insert_sort([1, 2, 3]))
print(insert_sort([1, 2, 7, 6, 8, 9, 0]))