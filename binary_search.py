
def binary_search(data, value):
	if len(data) == 0:
		return False
	middle_index = round(len(data) / 2)
	middle = data[middle_index]
	if value == middle:
		return True
	elif value > middle:
		return binary_search(data[middle_index+1:], value)
	else:
		return binary_search(data[0:middle_index], value)


print(binary_search([1, 2, 3], 0))
print(binary_search([1, 2, 3], 1))
print(binary_search([1, 2, 3], 2))
print(binary_search([1, 2, 3], 3))
print(binary_search([1, 2, 3], 4))
print(binary_search([1, 2, 3], 0))
print(binary_search([1, 2, 3, 4], 1))
print(binary_search([1, 2, 3, 4], 2))
print(binary_search([1, 2, 3, 4], 3))
print(binary_search([1, 2, 3, 4], 4))
print(binary_search([1, 2, 3, 4], 5))
print('Otro')

def binary_search_2(data, value, min, max):
	if min > max:
		return False
	middle_index = min + round((max - min) / 2)
	middle = data[middle_index]
	if value == middle:
		return True
	elif value > middle:
		return binary_search_2(data, value, middle_index + 1, max)
	else:
		return binary_search_2(data, value, 0, middle_index - 1)

print(binary_search_2([1, 2, 3], 0, 0, 2))
print(binary_search_2([1, 2, 3], 1, 0, 2))
print(binary_search_2([1, 2, 3], 2, 0, 2))
print(binary_search_2([1, 2, 3], 3, 0, 2))
print(binary_search_2([1, 2, 3], 4, 0, 2))
print(binary_search_2([1, 2, 3], 0, 0, 2))
print(binary_search_2([1, 2, 3, 4], 1, 0, 3))
print(binary_search_2([1, 2, 3, 4], 2, 0, 3))
print(binary_search_2([1, 2, 3, 4], 3, 0, 3))
print(binary_search_2([1, 2, 3, 4], 4, 0, 3))
print(binary_search_2([1, 2, 3, 4], 5, 0, 3))