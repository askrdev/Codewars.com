""" 
Codewars.com/Reversing Words in a String| 8 Kyu  
"""

"""
Task
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""

"""
Example input
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse('Hello World'), 'World Hello')
        test.assert_equals(reverse('Hi There.'), 'There. Hi')
"""

st1 = 'Hello World'
st2 = 'Hi There.'
st3 = "kontolpanjangbanget"
st4 = "rqlagyliuewwfflrki"
st5 = "htahsgftppijjyrluugtytdh"
st6 = "wgreofl roiaeuryujpseufprqgrlgighrtgwluikpoppekgsflwei  hsgjddihkdfekeiridkrqrrklgko o"

def reverse(st):
    # Your Code Here
    return " ".join(reversed(st.split(' '))) if st.count(" ") <= 1 else st   

print (reverse(st6))

# print(reversed(st2.split(" ")))

def reverse1(st):
    # Your Code Here
    to_list = st.split(" ")
    reverse = to_list[::-1]
    result = ""
    for i in reverse :
        result += " " + i
    return result.strip() if st.count(" ") <= 1 else st
print(reverse1(st1))
      