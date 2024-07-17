""" Codewars.com/doublechar 8 Kyu """

"""

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!

"""

string1 = "aku adalah seorang kapiten"
string2 = "aku bukanlah superstar"

def double_char(s):
    return "".join([a * 2 for a in s])

print(double_char(string2))