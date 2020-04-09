
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv
from backtrack import backtracking_search


for puzzle in [easy1, harder1]:
    s  = Sudoku(puzzle)  # construct a Sudoku problem
    raise NotImpelemented
