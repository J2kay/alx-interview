#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""


def retrieve_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_conflicting(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def solution_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for existing_solution in solutions:
        match_count = 0
        for pos1 in existing_solution:
            for pos2 in group:
                if pos1[0] == pos2[0] and pos1[1] == pos2[1]:
                    match_count += 1
        if match_count == n:
            return True
    return False


def construct_solution(row, group):
    """Builds a solution for the N queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        temp_solution = group.copy()
        if not solution_exists(temp_solution):
            solutions.append(temp_solution)
    else:
        for col in range(n):
            idx = (row * n) + col
            matches = zip([pos[idx]] * len(group), group)
            used_positions = map(lambda x: is_conflicting(x[0], x[1]), matches)
            group.append(pos[idx].copy())
            if not any(used_positions):
                construct_solution(row + 1, group)
            group.pop()


def find_solutions():
    """Finds the solutions for the given chessboard size."""
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    construct_solution(0, [])


n = retrieve_input()
find_solutions()
for solution in solutions:
    print(solution)
