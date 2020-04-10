

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        raise notImplemented
        """

        """
        # MRC will throw an error as all variables have been assigned.
        Thus, return solution when all variables are assigned.
        """
        if len(assignment)==81:
            return assignment

        unassigned_var = select_unassigned_variable(assignment, csp)
        if unassigned_var is not None:
            for domain in order_domain_values(unassigned_var, assignment, csp):
                removals=[]
                csp.assign(unassigned_var, domain, assignment)
                infer = inference(csp, unassigned_var, domain, assignment, removals) 
                if infer:
                    assignment = backtrack(assignment)
                    if csp.goal_test(assignment):
                        return assignment
                csp.unassign(unassigned_var, assignment)
                csp.restore(removals)
        return assignment

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
