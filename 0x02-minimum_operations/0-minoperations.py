#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
    """

    temp = 1
    initial = 0
    count = 0
    while temp < n:
        remainder = n - temp
        if (remainder % current == 0):
            initial = temp
            temp += initial
            count += 2
        else:
            temp += initial
            count += 1
    return count
