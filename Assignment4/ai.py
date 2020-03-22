import abstractstrategy
import checkerboard

class Strategy(abstractstrategy.Strategy):

    ## Alpha-beta pruning minimax search.
    def __init__(self, player, game, maxplies):
        super().__init__(player,game, maxplies)
        # super.__init__(player=player,game=game, maxplies=maxplies)

    def utility(self, board):
        "Return the utility of the specified board"
        playerId = board.playeridx(self.maxplayer)
        otherId = board.playeridx(self.minplayer)
        return board.pawnsN[playerId] + board.kingsN[playerId]*4 - board.pawnsN[otherId] - board.kingsN[otherId]*4
        
        # raise NotImplementedError("Subclass must implement")
    
    def play(self, board):
        """"play - Make a move
        Given a board, return (newboard, action) where newboard is
        the result of having applied action to board and action is
        determined via a game tree search (e.g. minimax with alpha-beta
        pruning).
        """
        print(self.maxplayer,' thinking using Alpha-Beta pruning strategy...')

        # result =  self.maxValue(board,0, float("-inf"), float("inf"))
        # print('Utility:', result[0])
        # return (board.move(result[1]), result[1])

        action =  self.maxValue(board,0, float("-inf"), float("inf"))[1]
        return (board.move(action), action)

    def maxValue(self, board,  depth, alpha, beta):
        if depth >= self.maxplies:
            return (self.utility(board),None)
        else:
            actions = board.get_actions(self.maxplayer)
            val = float('-inf')
            move = None
            for action in actions:
                newBoard = board.move(action)
                val = max(val, self.minValue(newBoard, depth+1, alpha, beta)[0])
                if val > alpha:
                    move = action
                if val >= beta:
                    break
                else:
                    alpha = max(alpha, val)
            return (val, move)

    def minValue(self, board,  depth, alpha, beta):
        if depth >= self.maxplies:
            return (self.utility(board),None)
        else:
            actions = board.get_actions(self.maxplayer)
            val = float('inf')
            move = None
            for action in actions:
                newBoard = board.move(action)
                val = min(val, self.maxValue(newBoard, depth+1, alpha, beta)[0])
                if val > beta:
                    move = action
                if val <= alpha:
                    break
                else:
                    beta = min(beta, val)
            return (val, move)