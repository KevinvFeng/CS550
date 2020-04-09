'''
Constraint propagation
'''
def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    csp.neighbors[x] is the neighbors of variable x
    raise NotImplemented
    """
    if not queue:
        variables = csp.variables
        queue = [ (var, neighbor) for var in variables for neighbor in csp.neighbors[var] ]

    while(queue):
        arc = queue.pop()
        if revise(csp, arc[0],arc[1]):
            if not csp.curr_domains[arc[0]]:
                break
            else:
                for neighbor in csp.neighbors[arc[0]]:
                  if neighbor != arc[1]:
                      queue.append((neighbor,arc[0])) 
    return csp
    
def revise(csp, Xi, Xj):
    revised = False
    assignment = csp.infer_assignment()
    domains = csp.curr_domains[Xi]
    for d_val in domains:
        if csp.nconflicts(Xi,d_val, assignment):
            csp.curr_domains[Xi].remove(d_val)
            revised= True
    return revised





