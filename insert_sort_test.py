
def insert_sort(data):
	for unsorted in range(1, len(data)):
		candidate = data[unsorted]
		new_location = unsorted
		for sorted in range(unsorted-1, 0, -1):
			if candidate < data[sorted]:
				new_location = sorted
				data[sorted+1] = data[sorted]
			else:
				break
		data[new_location] = candidate
	return data


print(insert_sort([1, 3, 2]))
print(insert_sort([1, 2, 3]))
print(insert_sort([3, 2, 1]))
print(insert_sort([1, 2, 1]))

