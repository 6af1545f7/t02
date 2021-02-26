# -*- coding: utf-8 -*-
"""
This is ...
"""

import sys

from t02 import __version__

__author__ = "6af1545f7"
__copyright__ = "6af1545f7"
__license__ = "mit"


def empty_board(w, h) :
    """Creates a rectangular empty board of the specified width and height.
    Returns:
    empty board"""
    b = []
    for j in range(h) :
        r = []
        for i in range(w) :
            r.append(None)
        b.append(r)
    return b


def populate(board, living_cells) :
    """Turns :on each of the cells in board specified as [y, x] coordinates.
    Returns:
        board"""
    b = board
    for c in living_cells:
        b[c[0]][c[1]] = ':on'
    return b


def board_print(board) :
    print('Board:', len(board), 'rows X', len(board[0]), 'colls')
    for r in board :
        print('      ', r)
    print(' ')
    return


def windows(coll) :
    """Yields windows centered around each item of coll,
    padded as necessary with None.
    Yields:
        3-item windows
    """
    cs = (None, *coll, None)
    for i in range(len(cs)) :
        if len(cs[i:i+3]) == 3 :
            yield cs[i:i+3]


def windows_print(window) :
    print('Windows:', window)
    for w in window :
        print('        ', w)
    print(' ')
    return


def cell_down(cell) :
    """Returns a vector cell below the input 'cell',
    or None if at the edge of the board.
    """
    c = None
    if cell is not None and cell[0] > 0 :
        c = [cell[0]-1, cell[1]]
    return c


def cell_up(cell, board_size) :
    """Returns a vector cell above the input 'cell',
    or None if at the edge of the board of 'board_size'.
    """
    c = None
    if cell is not None and cell[0] < board_size :
        c = [cell[0]+1, cell[1]]
    return c


def cell_block(window, board_size) :
    """'Window' is a triple of 3-item sequences, with maximum board_size.
    returns:
        tuple of 3x3 cells.
    """
    left = window[0]
    mid = window[1]
    right = window[2]
    ws = ((cell_down(left), cell_down(mid), cell_down(right)),
          window,
          (cell_up(left, board_size), cell_up(mid, board_size),
           cell_up(right, board_size)))
    return ws


def cell_block_print(cb) :
    print('Cell block:')
    for r in cb :
        print('           ', r)
    print(' ')
    return


def cell_state(cell, board) :
    state = None
    state = board[cell[0]][cell[1]]
    return state


def block_centre(block) :
    """
    Returns the cell at the centre of 3x3 'block'.
    """
    i = 0
    for row in block :
        for cell in row :
            i = i + 1
            if i == 5 :
                return cell
    return None


def liveness(block, board) :
    """
    'block' is a tuple of 3x3 cells on the 'board',
    that is centred on a live cell.
    A live cell with 2 or 3 live neighbours lives.
    A dead cell with exactly three live neighbours lives.
    Returns:
        liveness (None or :on) of the centre cell for the next step."
    """
    liveness = None
    count = 0
    bc = block_centre(block)
    centre_live = False
    if board[bc[0]] is not None :
        if board[bc[0]][bc[1]] is not None :
            centre_live = board[bc[0]][bc[1]] == ':on'
    for t in block :
        if t is not None :
            for c in t :
                if c is not None :
                    if cell_state(c, board) == ':on' :
                        count = count + 1
    if (count == 3) :
        liveness = ':on'
    if (count == 4 and centre_live) :
        liveness = ':on'
    print('centre live?', centre_live, 'count:', count, 'liveness:', liveness)
    return liveness


def live_cells_step(live_cells, board) :
    """
    Takes an array of 'live_cells' on the 'board' and performs a step.
    Returns:
        list of live cells, following step.
    """
    lcs = []
    for w in windows(live_cells) :
        cb = cell_block(w, 4)
        # cell_block_print(cb)
        if liveness(cb, board) == ':on' :
            cc = block_centre(cb)
            #  print('live cell:', cc)
            lcs.append(cc)
    return lcs


def board_step(board, live_cells) :
    h = len(board)
    w = len(board[0])
    b = populate(empty_board(w, h), live_cells)
    return b


def conway_run() :
    lcs = [[2, 0], [2, 1], [2, 2], [1, 2], [0, 1]]  # initial live cells
    b = populate(empty_board(6, 6), lcs)
    board_print(b)
    c = lcs  # ([2, 0], [2, 1], [2, 2], [2, 3])
    print('Live cells:', c)
    windows_print(windows(c))
    """
    for w in windows(c) :
        cb = cell_block(w, 4)
        cell_block_print(cb)
        # this is redundant (
        cc = block_centre(cb)
        if cc != w[1] :
            print('block_centre error: cell:', cc)
        # ) this is redundant
        li = liveness(cb, b)
        """
    c = live_cells_step(c, b)
    print('First step:-')
    print('New live cells:', c)
    b2 = board_step(b, c)
    board_print(b2)
    b = b2
    for i in range(2, 4) :
        print(i, 'nth step:-')
        c = live_cells_step(c, b)
        b = board_step(b, c)
        board_print(b)
    return {'board' : b, 'live cells' : lcs, 'new board' : b2}


def conway() :
    return {'conway' : conway_run()}
