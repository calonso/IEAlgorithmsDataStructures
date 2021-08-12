
def sequential_search(what, where):
	for i in range(len(where)):
		if where[i] == what:
			return True
	return False


print(sequential_search('Oranges', ['Apples', 'Oranges']))
print(sequential_search('Apples', ['Oranges']))
print(sequential_search(1, [1, 2, 3]))
