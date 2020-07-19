'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element)
which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
'''

class Node:
	def __init__(self, val = None):
		self.val = val
		self.both = id(self.val)

	def __repr__(self):
		return str(self.val)

id_map = dict()
id_map[id("a")] = a
id_map[id("b")] = b
id_map[id("c")] = c
id_map[id("d")] = d
id_map[id("e")] = e

class LinkedList:
	def __init__(self, head):
		self.head = head
		self.tail = head
		self.head.both = 0
		self.tail.both = 0

	def add(self, element):
		self.tail.both ^= id(element.val)
		element.both = id(self.tail.val)
		self.tail = element

	def get(self, index):
		print(self.head.both ^ )

linked_list = LinkedList(Node('a'))
linked_list.add(Node('b'))
print(linked_list.get(0))