"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = sum(1 for row in board for cell in row if cell != EMPTY)
    if count % 2 == 1:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    # check if action is valid
    if board[i][j] != EMPTY:
        raise Exception('invalid action')

    # perform action i, j in new board
    result_board = deepcopy(board)
    result_board[i][j] = player(board)

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    if winning_player == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        return max_value(board, float('-inf'), float('inf'))[1]
    return min_value(board, float('-inf'), float('inf'))[1]

def max_value(board, cur_max, cur_min):
    optimal_action = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = min_value(result(board, action), cur_max, cur_min)[0]
        cur_max = max(cur_max, test)
        if test > v:
            v = test
            optimal_action = action
        if cur_max >= cur_min:
            break
    return [v, optimal_action]

def min_value(board, cur_max, cur_min):
    optimal_action = None
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    for action in actions(board):
        test = max_value(result(board, action), cur_max, cur_min)[0]
        cur_min = min(cur_min, test)
        if test < v:
            v = test
            optimal_action = action
        if cur_max >= cur_min:
            break
    return [v, optimal_action]
