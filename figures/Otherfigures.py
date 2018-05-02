# -*- coding: utf-8  -*-

from .Figure import Figure

class King(Figure):

    def assert_legal_move(self, new_pos):
        pass

    @property
    def symbol(self):
        return 'K' + self.color


class Queen(Figure):

    def assert_legal_move(self, new_pos):
        pass

    @property
    def symbol(self):
        return 'Q' + self.color

class Knight(Figure):

    def assert_legal_move(self, new_pos):
        pass

    @property
    def symbol(self):
        return 'N' + self.color

class Bishop(Figure):

    def assert_legal_move(self, new_pos):
        pass

    @property
    def symbol(self):
        return 'B' + self.color
