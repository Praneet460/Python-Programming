"""
Name: problem_01.py
Title: Find PI to the Nth Digit
Purpose: Enter a number and have the program generate PI up to that many decimal places.
Author: Praneet Nigam
License: MIT

"""
# import necessary module
import math

# define a funtion
""" def <func-name> (frags, *args, **kwargs) """
def pi_upto(n, *args, **kwargs):
    """ assert <condition>, <message> """
    assert (n > 0), "Value should be greater than zero"
    if n > 50:
        return ("Value is too high. Please input the value under the range of 50.")
    else:
        return ("Value of pi = %.*f" %(n, math.pi))

""" Testing """
# print(pi_upto(5))
# print(pi_upto(0))
# print(pi_upto(20, 10, verbose = -1))
# print(pi_upto(-1))
# print(pi_upto(55))
