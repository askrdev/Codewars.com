""" 
Codewars.com/Thinkful - Logic Drills: Traffic light| 8 Kyu  
"""

"""
Task
You're writing code to control your town's traffic lights. 
You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing 
the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.
"""

"""
Example input
test.assert_equals(update_light('green'), 'yellow')
        test.assert_equals(update_light('yellow'), 'red')
        test.assert_equals(update_light('red'), 'green')
"""
current = 'yellow'

def update_light(current):
    return 'yellow' if current == 'green' else 'red' if current == 'yellow' else 'green'

print(update_light(current))

"""

## jawaban yang simple
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

print(update_light(current))
"""