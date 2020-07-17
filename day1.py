'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Approach #1 (WORKS :D):
	Edge: list empty, k < 0
	1). Loop through the list
	2). If the current number is not bigger than k:
		3). If the stack is not empty:
			see if any number in the stack added to the current number equal k
			if it does:
				return true
	4). Return false by default

Approach #2:
	{7, 2, 14, 7}
'''

arr2 = [10, 15, 3, 7]
# def check_if_adds_to_k(arr, k):
# 	# Edge: Invalid list, or k is not an int return false
# 	if not arr or not isinstance(k, int):
# 		return False

# 	# Make a copy of the list, to avoid changing the original
# 	arr = arr[:]

# 	previous = []
# 	# Loop through the copy since we would be changing the array in place
# 	for number in arr[:]:
# 		if number < k:
# 			previous.append(arr.pop(0))
# 			for prev_number in previous:
# 				if number + prev_number == k:
# 					return True
# 		else:
# 			# Return false because the current number is larger than k
# 			return False

# 	return False

def check_if_adds_to_k(arr, k):
	if not arr or not isinstance(k, int):
		return False

	potential_solutions = set()
	for num in arr:
		if num in potential_solutions:
			return True
		else:
			potential_solutions.add(k - num)

	return False
	
print(check_if_adds_to_k(arr2, 25))
print(arr2)