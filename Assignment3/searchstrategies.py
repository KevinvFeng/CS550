"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is at the bottom right, e.g.:
        123
        456
        78
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
 
class BreadthFirst:
    "BredthFirst - breadthfirst search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        if parentnode:
            # print('Cost:  ', parentnode.get_g+1)
            return parentnode.get_g()+1
        else:
            return 0

    @classmethod
    def h(cls, state):
        return 0
        # return appropriate h value

class DepthFirst:
    "DepthFirst - depth first search"
    @classmethod
    def g(cls, parentnode, action, childnode): #To be h()
        # max_depth = 20
        max_depth = 4
        if parentnode:
            if childnode.depth > max_depth:
                return 0
                # return -childnode.depth+1
            else:
                return -childnode.depth
        else:
            return 0
        # return appropritate g value

    @classmethod
    def h(cls, state): #To be g()
        return 1
        # return appropriate h value

class Manhattan:
    "Manhattan Block Distance heuristic"
    @classmethod
    def g(cls, parentnode, action, childnode):
        if parentnode:
            return parentnode.get_g()+1
        else:
            return 0
        # return appropritate g value

    @classmethod
    def h(cls, state):
        (row, col) = state.empty
        return state.boardsize*2-row-col
        # return appropriate h value