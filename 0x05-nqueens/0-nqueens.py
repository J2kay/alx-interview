#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(sys.argv[1])

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ solve """
    for solution in queens(n):
        result = []
        for i in range(n):
            result.append([i, solution[i]])
        print(result)


solve(N)
