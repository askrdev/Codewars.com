""" 
Codewars.com/Pillars| 8 Kyu  
"""

"""
Task
There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. 
Your function accepts three arguments:

number of pillars (≥ 1);
distance between pillars (10 - 30 meters);
width of the pillar (10 - 50 centimeters).
Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).
"""

"""
Example input
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(pillars(1, 10, 10), 0)
        test.assert_equals(pillars(2, 20, 25), 2000)
        test.assert_equals(pillars(11, 15, 30), 15270)
"""

num_pill, dist, width = (1, 10, 10)
def pillars(num_pill, dist, width):
    return (num_pill - 1) * (dist * 100) + (width * num_pill) - (2 * width) if num_pill > 1 else 0

# print((num_pill - 1) * (dist * 100) + (width * num_pill) - (2 * width))
# print((2-1)*(20 * 100)+(25*2) - (2 *25))

print (pillars(num_pill, dist, width))