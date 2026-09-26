#leetcode#37. Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Using backTracking to solve the sudoku puzzle. The function iterates
        through each cell in the board, and for each empty cell (denoted by '.'),
        it tries to fill it with digits from '1' to '9'. For each digit, it checks
        if placing that digit in the current cell is valid according to Sudoku rules
        (i.e., the digit does not already exist in the same row, column, or 3x3 sub-box).
        If a valid digit is found, it places the digit and recursively attempts to solve
        the rest of the board. If it reaches a point where no valid digit can be placed,
        it backtracks by resetting the cell to '.' and trying the next digit. This process continues until the entire board is filled correctly.
        """
        # solve using sets to track the numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            for num in map(str, range(1, 10)):
                box_index = (r // 3) * 3 + (c // 3)
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if backtrack(r, c + 1):
                        return True

                    # backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0, 0)