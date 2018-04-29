# -*- coding: utf-8 -*-

class Pawn(object):
    def __init__(self, color, pos):
        self.__color = color
        self.__pos   = pos

    @property
    def color(self):
        return self.__color

    @property
    def symbol(self):
        return 'p'+self.color

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        x0, y0 = self.pos
        x1, y1 = value
        if self.color == 'b':
            if y0-y1 !=1 or x0 != x1:
                raise InvalidMove()
        else:
            if y1-y0 !=1 or x0 != x1:
                raise InvalidMove()
        self.__pos = value
    # comm
