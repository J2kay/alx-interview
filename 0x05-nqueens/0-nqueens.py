#!/usr/bin/python3
"""N queens solution finder module."""
import sys


def retrieve_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
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


def find_solutions(n):
    """Finds and prints all solutions for the given chessboard size."""
    def construct_solution(row, group):
        """Builds a solution for the N queens problem.

        Args:
            row (int): The current row in the chessboard.
            group (list of lists of integers): The group of valid positions.
        """
        if row == n:
            solutions.append(group.copy())
        else:
            for col in range(n):
                idx = (row * n) + col
                matches = zip([positions[idx]] * len(group), group)
                if not any(map(lambda x: is_conflicting(x[0], x[1]), matches)):
                    group.append(positions[idx])
                    construct_solution(row + 1, group)
                    group.pop()

    solutions = []
    positions = [[i // n, i % n] for i in range(n * n)]
    construct_solution(0, [])

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    n = retrieve_input()
    find_solutions(n)
