
def bubble_sort(data):
	for i in range(len(data)):
		for j in range(len(data)-i-1):
			if data[j] > data[j+1]:
				temp = data[j]
				data[j] = data[j+1]
				data[j+1] = temp
	return data


print(bubble_sort([3, 6, 2, 1]))

