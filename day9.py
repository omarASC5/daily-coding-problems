'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''

def findLargestSum(array):
    if not array or len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        return max(array[0], array[1])

    dp = [None] * (len(array))
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        dp[i] = max(array[i] + dp[i - 2], dp[i - 1])

    return dp[len(array) - 1]

print(findLargestSum([2, 4, 6, 8])) # 12
print(findLargestSum([5, 1, 1, 5])) # 10
print(findLargestSum([1,2,3,1])) # 4
print(findLargestSum([2,7,9,3,1])) # 12
