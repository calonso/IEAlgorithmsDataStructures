
class Queue:
	def push(box):
		pass

	def pop(box):
		pass

	def empty():
		pass

class Box:
	def open():
		pass

class Item:
	def is_key():
		pass


def iterative_grandmas_attic(box):
	queue = Queue()
	while not queue.empty():
		items = box.open()
		for item in items:
			if item.is_key():
				print "Found the key!"
			else:
				queue.push(box)


def recursive_grandmas_attic(box):
	items = box.open()
	for item in items:
		if item.is_key():
			print "Found the key"
		else:
			recursive_grandmas_attic(item)
