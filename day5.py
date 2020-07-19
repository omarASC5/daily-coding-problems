'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair_func):
	# Pass in a function that accepts the two numbers and makes
	# a pair as a tuple, then return [0] or [1] respectively
	return (pair_func(lambda a, b: (a, b)))[0]

def cdr(pair_func):
	return (pair_func(lambda a, b: (a, b)))[1]

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))