'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26,
and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.
'1' + '11'
'11' + '1'
'111'
You can assume that the messages are decodable. For example, '001' is not allowed.

1). Make char_map

'''

char_map = {
	'1': 'a', '2': 'b', '3': 'c',
	'4': 'd', '5': 'e', '6': 'f',
	'7': 'g', '8': 'h', '9': 'i',
	'10': 'j', '11': 'k', '12': 'l',
	'13': 'm', '14': 'n', '15': 'o',
	'16': 'p', '17': 'q', '18': 'r',
	'19': 's', '20': 't', '21': 'u',
	'22': 'v', '23': 'w', '24': 'x',
	'25': 'y', '26': 'z'
}

def helper(data, k, memo):
	if k == 0:
		return 1
	s = len(data) - k
	if data[s] == '0':
		return 0
	if memo[k] != None:
		# Check if the current function call was already memoized
		return memo[k]

	# First, consider one numner at a time
	result = helper(data, k - 1, memo)
	# Then, consider a two digit number
	if k >= 2 and int(data[s:s + 2]) <= 26:
		result += helper(data, k - 2, memo)

	# Memoize the function result
	memo[k] = result
	return result

def num_ways(data):
	# Make a memo list to memoize previous function calls
	memo = [None] * (len(data) + 1)
	return helper(data, len(data), memo)

print(num_ways('111111'))