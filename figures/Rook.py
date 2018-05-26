# -*- coding: utf-8 -*-
from exceptions import InvalidMove
from .Figure import Figure


class Rook(Figure):

    def assert_legal_move(self, new_pos):
        x0, y0 = self.pos
        x1, y1 = new_pos
        if x0 != x1 and y0 != y1:
            raise InvalidMove
        else:
            pass

    @property
    def symbol(self):
        return 'R' + self.color
