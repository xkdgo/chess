# -*- coding: utf-8  -*-

class Figure(object):
    def __init__(self, color, pos):
        self.__color = color
        self.__pos = pos

    def assert_legal_move(self, new_pos):
        raise NotImplementedError('Method is abstract')

    @property
    def color(self):
        return self.__color

    @property
    def symbol(self):
        raise NotImplementedError('Property is abstract')

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, value):
        self.assert_legal_move(value)
        self.__pos = value
