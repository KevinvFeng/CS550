'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue 
from explored import Explored

# import time

def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.

    If debug is True, debugging information will be displayed.

    if verbose is True, the following information will be displayed:

        Number of moves to solution
        List of moves and resulting puzzle states
        Example:

            Solution in 25 moves
            Initial state
                  0        1        2
            0     4        8        7
            1     5        .        2
            2     3        6        1
            Move 1 -  [0, -1]
                  0        1        2
            0     4        8        7
            1     .        5        2
            2     3        6        1
            Move 2 -  [1, 0]
                  0        1        2
            0     4        8        7
            1     3        5        2
            2     .        6        1

            ... more moves ...

                  0        1        2
            0     1        3        5
            1     4        2        .
            2     6        7        8
            Move 22 -  [-1, 0]
                  0        1        2
            0     1        3        .
            1     4        2        5
            2     6        7        8
            Move 23 -  [0, -1]
                  0        1        2
            0     1        .        3
            1     4        2        5
            2     6        7        8
            Move 24 -  [1, 0]
                  0        1        2
            0     1        2        3
            1     4        .        5
            2     6        7        8

        If no solution were found (not possible with the puzzles we
        are using), we would display:

            No solution found

    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    # start = time.time()

    initial_node = Node(problem, problem.initial)
    node_queue = PriorityQueue(f=lambda x: x.get_f())
    explore = Explored()
    explore.add(initial_node.state)
    node_num = 1
    node = initial_node
    board = problem.initial
    solved = board.solved()

    while(not solved):
        newNodes = node.expand(problem)
        #Insert all new nodes into queues and explored
        for newNode in newNodes:
            if not explore.exists(newNode.state):
                explore.add(newNode.state)
                node_queue.append(newNode)
                node_num +=1
                if newNode.state.solved():
                    node = newNode
                    solved = newNode.state.solved()
                    break #?
        if len(node_queue)==0:
            break

        if not solved:
            node = node_queue.pop()
            board =newNode.state


    # second = (time.time() - start)
    actions = node.path()
    solutions = node.solution()
    if verbose:
        if len(solutions)==0:
            print("No solution found")
        else:
            for k,v in enumerate(actions):
                if k == 0:
                    print("Solution in {} moves".format(len(actions)-1))
                    print("Initial state")
                else:
                    print("Move {} -  {}".format(k,solutions[k-1]))
                print(v.state)
        # for item in actions:
        #     print(item)
    # actions = [a_node.action for a_node in node.path() if a_node.action]
    # return (actions, node_num, second)
    return (actions, node_num)
#     raise NotImplemented
