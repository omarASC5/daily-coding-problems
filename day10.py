'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''
import time

def jobScheduler(n, function, *args, **kwargs):
    time.sleep(n / 1000)
    function(*args, **kwargs)

def test(string, string2, string3='so'):
    print(string, string2, string3)

print(jobScheduler(1000, test, "hi", "omar", "bro"))
