'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
'''

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def unival_count(root):
    count = 0
    def helper(node):
        # Source for scoping: https://stackoverflow.com/questions/5218895/python-nested-functions-variable-scoping
        nonlocal count
        if not node:
            # Leaf nodes are univalue
            return 1

        left = helper(node.left)
        right = helper(node.right)
        
        if left and right:
            if (node.left and node.left.val != node.val) or \
               (node.right and node.right.val != node.val):
                return 0

            count += 1
            return 1

        return 0

    helper(root)
    print(count, count)
    return count

node1 = Node(0)
node2 = Node(1)
node3 = Node(0)
node4 = Node(1)
node5 = Node(1)
node6 = Node(1)
node7 = Node(0)

node1.left = node2
node4.left = node5
node4.right = node6
node3.left = node4
node3.right = node7
node1.right = node3

print(unival_count(node1))
#assert unival_count(node2) == 1
#assert unival_count(node5) == 1
#assert unival_count(node1) == 5
