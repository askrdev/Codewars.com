""" 
Codewars.com/Function 2 - squaring an argument| 8 Kyu  
"""

"""
Task
Now you have to write a function that takes an argument and returns the square of it.
"""

"""
Example input
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square(2), 4)
        test.assert_equals(square(50), 2500)
        test.assert_equals(square(1), 1)
"""

def square(n):
    return n ** 2

print(square(2))