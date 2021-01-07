'''
This problem was asked by Google.

The area of a circle is defined as r^2. Estimate \pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
'''
import random

def estimatePi():
    a_square = 0
    a_circle = 0
    r = (10 ** 8)
    while a_square < r:
        x = random.randint(0, r)
        y = random.randint(0, r)
        # Calculate number of points in circle
        if ((x ** 2) + (y ** 2)) < r ** 2:
            a_circle += 1
        # Calculate number of points in square
        a_square += 1

    # Ac = PI * (r^2), As = (2r)(2r) = 4r^2
    # Ac / As = PI / 4
    return 4 * (a_circle / a_square)

print(estimatePi())
