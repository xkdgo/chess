# -*- coding: utf-8 -*-

from exceptions import InvalidMove
from .Figure import Figure


class Pawn(Figure):
    def __init__(self, color, pos):
        super().__init__(color, pos)

    def assert_legal_move(self, new_pos):
        x0, y0 = self.pos
        x1, y1 = new_pos
        if self.color == 'b':
            if y0 - y1 != 1 or x0 != x1:
                raise InvalidMove()
        elif y1 - y0 != 1 or x0 != x1:
                raise InvalidMove()
        else:
            pass

    @property
    def symbol(self):
        return 'p' + self.color
