'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:
'leftleft.leftright'
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''
from collections import deque

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def	serialize(node):
	if node == None:
		return 'X'

	serialized_left = serialize(node.left)
	serialized_right = serialize(node.right)

	return node.val + ',' + serialized_left + ',' + serialized_right

def deserialize(string):
	# Initializing the queue
	# Adding tree elements to queue
	queue = deque(string.split(','))

	# Process the queue in a separate function
	return deserialize_helper(queue)

def deserialize_helper(queue):
	# Pop the next node from the front of the queue
	current_node = queue.popleft()
	# If the current node is 'X' that means it is equivalent to NULL
	if current_node == 'X':
		return None

	# Make a new node with the node next in the queue
	new_node = Node(current_node)
	new_node.left = deserialize_helper(queue)
	new_node.right = deserialize_helper(queue)

	return new_node

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
