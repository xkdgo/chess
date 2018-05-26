# -*- coding: utf-8 -*-

from Board import Board

brd = Board(8)
brd.initialize()

while True:
    brd.show()
    move_text = input(': ')
    brd.move(move_text)