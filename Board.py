# -*- coding: utf-8 -*-

import figures as fg
from figures import Figure
from exceptions import InvalidPosition, PositionOccupied, InvalidMove
from helpers import str_to_move

class Board(object):
    def __init__(self, height=8, width=None):
        self.__height = height
        if width is None:
            self.__width = self.__height
        else:
            self.__width = width
        self.__figures = []

    def __contains__(self, val):
        if isinstance(val, Figure):
            # return any(( x is val for x in self.__figures ))
            for x in self.__figures:
                if x is val:
                    return True
            else:
                return False
        else:
            x, y = val
            if x < 0 or x >= self.width:
                return False
            if y < 0 or y >= self.height:
                return False
            return True

    def __getitem__(self, pos):
        x, y = pos
        if isinstance(x, slice) or isinstance(y, slice):
            raise NotImplementedError('Slice indexing not implemented')
        # TODO if position right
        for f in self.__figures:
            if f.pos == (x, y):
                return f
        else:
            return None

    def add(self, fig):
        # добавляет фигуру на доску
        if fig in self:
            # fig in self call method __contains__
            return
        if not (fig.pos in self):
            # fig.pos in self call method __contains__
            raise InvalidPosition(fig.pos)
        x, y = fig.pos

        if self[x, y] is not None:
            # self[x, y] call method __getitem__
            raise PositionOccupied()
        self.__figures.append(fig)
        fig.board = self
        # используется сеттер из Figure
        # создает слабую ссылку на доску

    def take_from_pos(self, pos):
        # снимает фигуру с доски и возвращает ссылку на эту фигуру
        # используется перебор списка по индексу
        for k in range(0,len(self.__figures)):
            if self.__figures[k].pos == pos:
                x = self.__figures[k]
                del self.__figures[k]
                return x
        return None

    def initialize(self):
        for i in range(0, self.width):
            f = fg.Pawn('w', (i, 1))
            self.add(f)
            # self.add call method add
            f = fg.Pawn('b', (i, self.height - 2))
            self.add(f)
        last = self.height - 1
        self.add(fg.Rook('w', (0, 0)))
        self.add(fg.Rook('w', (7, 0)))
        self.add(fg.Rook('b', (0, last)))
        self.add(fg.Rook('b', (7, last)))

        self.add(fg.Knight('w', (1, 0)))
        self.add(fg.Knight('w', (6, 0)))
        self.add(fg.Knight('b', (1, last)))
        self.add(fg.Knight('b', (6, last)))

        self.add(fg.Bishop('w', (2, 0)))
        self.add(fg.Bishop('w', (5, 0)))
        self.add(fg.Bishop('b', (2, last)))
        self.add(fg.Bishop('b', (5, last)))

        self.add(fg.Queen('w', (3, 0)))
        self.add(fg.King('w', (4, 0)))

        self.add(fg.Queen('b', (3, last)))
        self.add(fg.King('b', (4, last)))



    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def __str__(self):
        return f'<board {self.height}x{self.width}>'

    __repr__ = __str__

    def show(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'[:self.width]
        print('     ' + (' ' * 5).join(alpha))
        # raise NotImplementedError('Board.show')
        print('  \u250c' + '\u2500' * 6 * self.width + '\u2510')
        for n in range(self.height, 0, -1):
            line = ('\u2588' * 6 + '\u2591' * 6) * self.width
            if n % 2 > 0:
                line = line[6:]
            line = line[:self.width * 6]
            line1 = '  \u2502' + line + '\u2502'
            # print figure on the board
            for k in range(0, self.width):
                f = self[k, n - 1]
                # self[k, n - 1] call method __getitem__
                if f is None:
                    # if __getitem__ returned None check next position k
                    continue
                b = k * 6 + 2
                c = b + len(f.symbol)
                line = line[:b] + f.symbol + line[c:]
            line2 = f'{n:2d}\u2502' + line + f'\u2502{n:2d}'
            print(line1)
            print(line2)
            print(line1)
        print('  \u2514' + '\u2500' * 6 * self.width + '\u2518')
        print('     ' + (' ' * 5).join(alpha))

    def move(self, fig_sym, start=None, finish=None, takes=False):
        # метод распаковывает строку введенную пользвателем
        # и передвигает фигуру
        # использует функцию str_to_move из helpers
        if isinstance(fig_sym, str):
            fig_sym, start, finish, takes = str_to_move(fig_sym)
        fig = self[start]
        # call func __getitem__(self, start)
        if fig is None:
            raise InvalidMove('Field is empty')
        if fig.symbol[0] != fig_sym:
            raise InvalidMove('Invalid figure')
        #  Проверить, еще что-то можно дописать проверки
        try:
            fig.pos = finish
        except PositionOccupied:
            self.take_from_pos(finish)
            fig.pos = finish

if __name__ == '__main__':
    x = Board(8)
    x.initialize()
    x.show()
