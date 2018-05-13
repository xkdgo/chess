# -*- coding: utf-8 -*-

_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
_DIGITS  = '123456789'

def str_to_pos(text):
    x = _LETTERS.index(text[0].lower())
    y = _DIGITS.index(text[-1].lower())
    return ( x, y )

def str_to_move(text):
    fig = text[0]
    start = str_to_pos(text[1:3])
    take = text[3].lower() == 'x'
    end = str_to_pos(text[4:5])
    return ( fig, start, end, take )
