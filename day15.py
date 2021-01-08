'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''
import random

count = 0
result = None

def chooseRandomFromStream(item):
    # This is based off the reservoir sampling technique from statistics
    global count
    global result

    count += 1
    if count == 1:
        result = item
    else:
        i = random.randint(0, count - 1)
        if i == count - 1:
            result = item

    return result

sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, element in enumerate(sample_stream):
    random_element = chooseRandomFromStream(element)
    print("Random element of the first {} is {}".format(index + 1, random_element))
