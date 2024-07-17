""" 
Codewars.com/They say that only 
the name is long enough to attract attention. 
They also said that only a simple Kata will have someone to solve it. 
This is a sadly story #1: Are they opposite? 8 Kyu 
"""

"""
Task
Give you two strings: s1 and s2. If they are opposite, return true; 
otherwise, return false. Note: The result should be a boolean value, instead of a string.

The opposite means: All letters of the two strings are the same, but the case is opposite. 
you can assume that the string only contains letters or it's a empty string. 
Also take note of the edge case - if both strings are empty then you should return false/False.

Examples (input -> output)
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false

######
Test Code
test.assert_equals(is_opposite("ab","AB") , True);
        test.assert_equals(is_opposite("aB","Ab") , True);
        test.assert_equals(is_opposite("aBcd","AbCD") , True);
        test.assert_equals(is_opposite("AB","Ab") , False);
        test.assert_equals(is_opposite("","") , False);
######
"""
s1 = 'AB'
s2 = 'ab'

def is_opposite(s1,s2):
    return False if s1 == '' and s2 == '' else False if s1[::len('A' if len(s1) == '' else len(s1))] == s2[::len('A' if len(s2) == '' else len(s2))] else True

# print(is_opposite(s1,s2))

#Versi Simple
def is_opposite(s1,s2):
    return s1 == s2.swapcase() if s1 else False

# print(is_opposite(s1,s2))

print(s1 == s2.swapcase())
print(s1.lower())
print(s2.swapcase())
