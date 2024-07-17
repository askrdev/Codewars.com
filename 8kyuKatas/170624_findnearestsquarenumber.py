""" 
Codewars.com/Find Nearest square number | 8 Kyu  
"""

"""
Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, 
the square of 11, than 100, the square of 10.

If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)

Check my other katas:

Alphabetically ordered

Case-sensitive!

Not prime numbers
"""

"""
Example Input
def basic_test_cases():
        test.assert_equals(nearest_sq(1), 1)
        test.assert_equals(nearest_sq(2), 1)
        test.assert_equals(nearest_sq(10), 9)
        test.assert_equals(nearest_sq(111), 121)
        test.assert_equals(nearest_sq(9999), 10000)
"""

n = 10

def nearest_sq(n):
    return round(n ** 0.5 ) ** 2

print (nearest_sq(n))

# print(round(n **  0.5))
