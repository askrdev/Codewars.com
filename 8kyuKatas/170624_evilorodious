""" Codewars.com/evilorodious 8 Kyu """

"""

The number n is Evil if it has an even number of 1's in its binary representation.
The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary representation.
The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, function should 
return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

good luck :)

"""

evil = [3, 5, 6, 9, 10, 12, 15, 17, 18, 20]
odious = [1, 2, 4, 7, 8, 11, 13, 14, 16, 19]

def evil(n):
    return "It's Evil!" if bin(n).count("1")%2 == 0  else "It's Odious!"

y = 6
## 5 = 0b101 --> 0
## 4 = 0b100 --> 1
## 3 = 0b11 --> 0
## 2 = 0b10 --> 1
## 1 = 0b1 --> 1
print (evil(7))

print (bin(y))
print(bin(y).count("1")%2)