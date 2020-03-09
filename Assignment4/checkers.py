'''
@author: mroch
'''

# Game representation and mechanics
import checkerboard

# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.7 and 3.8 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.  Big sister is watching you :-)

# Python cand load compiled modules using the imp module (deprecated)
# We'll format the path to the tonto module based on the
# release of Python.  Note that we provided tonto compilations for Python 3.7
# and 3.8.  If you're not using one of these, it won't work.
import imp
import sys
major = sys.version_info[0]
minor = sys.version_info[1]
modpath = "__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
tonto = imp.load_compiled("tonto", modpath)


# human - human player, prompts for input    
import human

import boardlibrary # might be useful for debugging

from timer import Timer
        

def Game(red=human.Strategy, black=tonto.Strategy, 
         maxplies=10, init=None, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """

    # Don't forget to create instances of your strategy,
    # e.g. black('b', checkerboard.CheckerBoard, maxplies)

    ##----------------------------------------- Implement
    gameboard = checkerboard.CheckerBoard()
    redPlayer = red('r', checkerboard.CheckerBoard, maxplies)
    blackPlayer = black('b', checkerboard.CheckerBoard, maxplies)

    turn = True if firstmove == 0 else False
    if verbose:
        clock = Timer()
    move_cnt= 0
    while not gameboard.is_terminal()[0]:
        move_cnt+=1
        if turn:
            if verbose:
                gameboard = verboseMode(redPlayer,gameboard,clock)
            else:
                gameboard = ClearMode(redPlayer,gameboard)
            turn = not turn
        else:
            if verbose:
                gameboard = verboseMode(blackPlayer,gameboard,clock)
            else:
                gameboard = ClearMode(blackPlayer,gameboard)
            turn = not turn

    if verbose:
        print('Final board')
        print(gameboard)
        winner = gameboard.is_terminal()
        if not winner[1]:
            print('Game is a draw')
        else:
            print('Winner is', winner[1])

    return gameboard
    # raise NotImplemented

def verboseMode(player, gameboard, clock):
    print('Player {} turn'.format(player.maxplayer))
    print(gameboard)
    move_clock = Timer()
    (_,move) = player.play(gameboard)
    elapsed_move = move_clock.elapsed_s()
    elapsed_all = clock.elapsed_min()
    print('Move ', '{:-5}'.format(gameboard.movecount),'by {}:'.format(player.maxplayer),gameboard.get_action_str(move), 'Result:')
    gameboard = gameboard.move(move)
    print(gameboard)
    print('Pawn/King count: r {} R {} b {} B {}'.format(gameboard.pawnsN[0], gameboard.kingsN[0], gameboard.pawnsN[1], gameboard.kingsN[1]))
    print('Move: {:.3} s, Game: {:.4} min\n'.format(elapsed_move, elapsed_all))
    return gameboard

def ClearMode(palyer, gameboard):
    (_,move) = palyer.play(gameboard)
    gameboard = gameboard.move(move)
    return gameboard

            
if __name__ == "__main__":
    #Game(init=boardlibrary.boards["multihop"])
    #Game(init=boardlibrary.boards["StrategyTest1"])
    #Game(init=boardlibrary.boards["EndGame1"], firstmove = 1)
    Game()
        
        
        


        
                    
            
        

    
    
