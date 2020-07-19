
'''
Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive integer
that does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

[4, 3, -1, 1] -> [-1 , 1, 3, 4]: Something missing: return the missing number
[1, 2, 0] -> [0, 1, 2] If nothing missing: return 1 + last_in_array
1). Loop through the array
3). If negative skip the value
4). Keep track of the lowest number
'''

def find_missing_num(array):
	# Make sure we are only working with lists
	if not isinstance(array, list):
		return None

	# Sort the array so we can find which number is not in its place
	array.sort()
	for i in range(len(array) - 1):
		# Ensure we are only considering positive numbers
		if array[i + 1] > 0 and array[i] > 0:
			# If the difference between the two positive adjacent elements is not zero
			# The number missing is +1 the current number
			if (array[i + 1] - array[i]) != 1:
				return array[i] + 1

	return array[-1] + 1

print(find_missing_num([4, 3, -1, 1]))
print(find_missing_num([1, 2, 0]))