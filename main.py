# -*- coding: utf-8 -*-

from Board import Board

brd = Board(8)
brd.initialize()

while True:
    brd.show()
    move = inpit(': ')
    f, s, e, t = str_to_move(move)