"""
Name: problem_03.py
Title: Fibonacci Sequence
Purpose: Enter a number and have the program generate the fibonacci sequence up to that many places.
Aurthor: Praneet Nigam
License: MIT

"""

# define a function
""" def <func-name> (fargs, *args, **kwargs) """
def fiboSeq_upto(n, *args, **kwargs):
    """ assert <condition>, <message> """
    assert (n > 0), "Value should be greater than zero."
    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    
    for i in series:
        series = str(series)
    
    return series

""" Testing """
# print(fiboSeq_upto(5))
# print(fiboSeq_upto(0))
# print(fiboSeq_upto(20))
# print(fiboSeq_upto(100, 8, verbose=-8))
# print(fiboSeq_upto(-1))