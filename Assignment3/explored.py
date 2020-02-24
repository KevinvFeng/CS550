'''

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.explored_set = set() # set is faster than list.
        # raise NotImplemented

    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        return hash(state) in self.explored_set
        # raise NotImplemented

    def add(self, state):
        """add(state) - add given state to the explored set.
        state must be hashable and we asssume that it is not already in set
        """
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

        self.explored_set.add(hash(state))
        # raise NotImplemented
            
