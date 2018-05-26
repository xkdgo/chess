# -*- coding: utf-8  -*-
from weakref import ref
# импортируем модуль слабой ссылки
from exceptions import InvalidPosition, PositionOccupied

class Figure(object):
    def __init__(self, color, pos, board=None):
        self.__color = color
        self.__pos = pos
        if board is None:
            self.__board = None
        else:
            self.__board = ref(board)
            # создаем слабую ссылку на доску

    def assert_legal_move(self, new_pos):
        raise NotImplementedError('Method is abstract')

    @property
    def board(self):
        if self.__board is None:
            return None
        else:
            return self.__board()
            # возвращается настоящая ссылка на доску

    @board.setter
    def board(self, value):
        if value is None:
            self.__board = None
        else:
            self.__board = ref(value)
            # создаем слабую ссылку на доску

    @board.deleter
    def board(self):
        # удаляем слабую ссылку
        self.__board = None

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
        if value not in self.board:
            # value - это новая позиция фигуры
            # self.board это getter возвращающий реальную ссылку на доску
            # таким образом
            # фраза in self.board вызывает метод __contains__
            # из класса Board, который возвращает False, если позиция вне доски
            raise InvalidPosition('Position is out of board')
        if self.board[value] is not None:
            raise PositionOccupied()

        self.assert_legal_move(value)
        self.__pos = value
