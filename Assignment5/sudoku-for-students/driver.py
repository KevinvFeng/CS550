from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, forward_checking, first_unassigned_variable, unordered_domain_values, no_inference
from backtrack import backtracking_search

for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)  # construct a Sudoku problem
    print("---initial state---")
    s.display(s.infer_assignment())
    print("\n")
    AC3(s)

    print("---after AC3---")
    s.display(s.infer_assignment())
    print("\n")

    if not s.goal_test(s.curr_domains):
        solved = backtracking_search(s, select_unassigned_variable=mrv, inference=forward_checking)
        print("---after backtracking---")
        s.display(solved)
