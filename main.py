# -*- coding: utf-8 -*-

from Board import Board

brd = Board(8)
brd.initialize()

while True:
    brd.show()
    move_text = inpit(': ')
    f, s, e, t = str_to_move(move_text)
    brd.move(f, s, e, t)