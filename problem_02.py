"""
Name: problem_02.py
Title: Find e to the Nth Digit
Purpose: Enter a number and have the program generate 'e' value up to that many decimal places.
Aurthor: Praneet Nigam
License: MIT

"""

# import necessary module
import math

# define a function
""" def <func-name> (fargs, *args, **kwargs) """
def e_upto(n, *args, **kwargs):
    """ assert <condition>, <message> """
    assert (n>0), "Value should be greater than zero."
    if n > 50:
        return ("Value is too high. Please input the value under the range of 50.")
    else:
        return ("Value of e = %.*f" %(n, math.e))

""" Testing """
# print(e_upto(5))
# print(e_upto(0))
# print(e_upto(20, 10, verbose = -1))
# print(e_upto(-1))
# print(e_upto(55))