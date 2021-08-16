
def append(what, where):
	last_element = where
	while last_element['next']:
		last_element = last_element['next']
	last_element['next'] = what


list = { 'key': 'Apples', 'next': None }

append({'key': 'Oranges', 'next': None}, list)

print(list)


def search(what, where):
	while where:
		if where['key'] == what:
			return where
		else:
			where = where['next']
	return None


print(search('Oranges', list))
print(search('Milk', list))


def insert(what, where):
	temp = where['next']
	where['next'] = what
	what['next'] = temp


apples = search('Apples', list)
milk = { 'key': 'Milk', 'next': None }
insert(milk, apples)

print(list)

def delete(what, where):
	prev = where
	curr = where['next']
	while curr['key'] != what:
		prev = curr
		curr = curr['next']
	prev['next'] = curr['next']

delete('Milk', list)
print(list)



