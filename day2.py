'''
	This problem was asked by Uber.

	Given an array of integers, return a new array such that each element at
	index i of the new array is the product of all the numbers in the
	original array except the one at i.

	For example, if our input was [1, 2, 3, 4, 5],
	the expected output would be [120, 60, 40, 30, 24].
	If our input was [3, 2, 1], the expected output would be [2, 3, 6].

	a). make new_arr
	1). Multiply all the numbers in the array
	2). Loop through again and divide the current number by the multiplied total
		new_number = multiplied_total  / array[i]
		new_arr.push(new_number)
'''

# def check_mult(arr):
# 	# If given an empty array, return empty array
# 	if not arr:
# 		return []

# 	# Get the product of multiplying every number in the array
# 	mult_sum = 1
# 	for num in arr:
# 		mult_sum *= num

# 	new_arr = []
# 	for num in arr:
# 		new_arr.append(int(mult_sum / num))
	
# 	return new_arr

def mult_array(arr):
	# Get the product of multiplying every number in the array
	mult_sum = 1
	if arr:
		for num in arr:
			mult_sum *= num

	return mult_sum

def check_mult(arr):
	# If given an empty array, return empty array
	if not arr:
		return []

	new_arr = []
	for i in range(len(arr[:])):
		# Remove the number at current index
		copy_arr = arr[:]
		copy_arr.pop(i)

		# Multiply all the other numbers in the array
		# Add that number to the new array
		new_arr.append(mult_array(copy_arr))
	
	return new_arr

print(check_mult([1, 2, 3, 4, 5]))