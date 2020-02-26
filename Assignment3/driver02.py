'''
Jinqi Cheng     RedID: 819472050 

Hsuan Yu Liu    RedID: 823327369
'''

'''
driver for graph search problem
'''
from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies
import pandas as pd

from multiprocessing import Process

class Timer:
    """Timer class
    Usage:
      t = Timer()
      # figure out how long it takes to do stuff...
      elapsed_s = t.elapsed_s() OR elapsed_min = t.elapsed_min()
    """

    def __init__(self):
        "Timer - Start a timer"
        self.s_per_min = 60.0  # Number seconds per minute
        self.start = time.time()

    def elapsed_s(self):
        "elapsed_s - Seconds elapsed since start (wall clock time)"
        return time.time() - self.start

    def elapsed_min(self):
        "elapsed_min - Minutes elapsed since start (wall clock time)"

        # Get elapsed seconds and convert to minutes
        return self.elapsed_s() / self.s_per_min

def driver() :

    numOfBoard = 31

    dfs_nodes = []
    dfs_elapsed = []
    dfs_length = []

    bfs_nodes = []
    bfs_elapsed = []
    bfs_length = []

    astar_nodes = []
    astar_elapsed = []
    astar_length = []

    for _ in range(numOfBoard):
        t = Timer()
        puzzle = NPuzzle(8,g=BreadthFirst.g, h = BreadthFirst.h)
        result = graph_search(puzzle,verbose=False)
        time_spent = t.elapsed_s()
        bfs_length.append(len(result[0]))
        bfs_nodes.append(result[1])
        bfs_elapsed.append(time_spent)

        t = Timer()
        puzzle = NPuzzle(8,g=DepthFirst.g, h = DepthFirst.h)
        result = graph_search(puzzle,verbose=False)
        time_spent = t.elapsed_s()
        dfs_length.append(len(result[0]))
        dfs_nodes.append(result[1])
        dfs_elapsed.append(time_spent)

        t = Timer()
        puzzle = NPuzzle(8,g=Manhattan.g, h = Manhattan.h)
        result = graph_search(puzzle,verbose=False)
        time_spent = t.elapsed_s()
        astar_length.append(len(result[0]))
        astar_nodes.append(result[1])
        astar_elapsed.append(time_spent)

    summary = pd.DataFrame(columns=['{:25}'.format('Measurements'),'{:25}'.format('BFS'), '{:25}'.format('DFS'),'{:25}'.format('A-Star')])
    summary.loc[0] = ['Length of plan(Mean)', mean(bfs_length),mean(dfs_length),mean(astar_length)]
    summary.loc[1] = ['Number of nodes(Mean)', mean(bfs_nodes),mean(dfs_nodes),mean(astar_nodes)]
    summary.loc[2] = ['Elapsed time(Mean)', mean(bfs_elapsed),mean(dfs_elapsed),mean(astar_elapsed)]
    summary.loc[3] = ['Length of plan(STD)', stdev(bfs_length),stdev(dfs_length),stdev(astar_length)]
    summary.loc[4] = ['Number of nodes(STD)', stdev(bfs_nodes),stdev(dfs_nodes),stdev(astar_nodes)]
    summary.loc[5] = ['Elapsed time(STD)', stdev(bfs_elapsed),stdev(dfs_elapsed),stdev(astar_elapsed)]
    print (summary.to_string(index=False))
    

    # raise NotImplemented
def driver_strategy(strategy):
    numOfBoard = 31
    nodes = []
    elapsed = []
    length = []
    strategy_name = ["BFS","DFS","Manhattan"]
    for _ in range(numOfBoard):
        t = Timer()
        if strategy == 0:
            puzzle = NPuzzle(8,g=BreadthFirst.g, h = BreadthFirst.h)
        elif strategy == 1:
            puzzle = NPuzzle(8,g=DepthFirst.g, h = DepthFirst.h)
        else:
            puzzle = NPuzzle(8,g=Manhattan.g, h = Manhattan.h)
        # result = graph_search(puzzle,verbose=True)
        result = graph_search(puzzle)
        time_spent = t.elapsed_s()
        length.append(len(result[0]))
        nodes.append(result[1])
        elapsed.append(time_spent)

    summary = pd.DataFrame(columns=['{:<30}'.format('Measurements'),'{:15}'.format(strategy_name[strategy])])
    summary.loc[0] = ['Length of plan(Mean)', mean(length)]
    summary.loc[1] = ['Number of nodes(Mean)', mean(nodes)]
    summary.loc[2] = ['Elapsed time(Mean)', mean(elapsed)]

    summary.loc[3] = ['Length of plan(STD)', stdev(length)]
    summary.loc[4] = ['Number of nodes(STD)', stdev(nodes)]
    summary.loc[5] = ['Elapsed time(STD)', stdev(elapsed)]
    
    print(format(strategy_name[strategy]))
    print (summary.to_string(index=False))


def driver_multiprocessing():
    p_bfs = Process(target=driver_strategy, args=(0,))
    p_dfs = Process(target=driver_strategy, args=(1,))
    p_man = Process(target=driver_strategy, args=(2,))
    p_bfs.start()
    p_dfs.start()
    p_man.start()
    p_bfs.join()
    p_dfs.join()
    p_man.join()
    
if __name__ == '__main__':
    driver_multiprocessing()
    # driver()
