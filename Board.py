# -*- coding: utf-8 -*-

class Board(object):
    def __init__(self, height=8, width=None):
        self.__height = height
        if width is None:
            self.__width = self.__height
        else:
            self.__width = width

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
        print('     '+(' '*5).join(alpha) )
        #raise NotImplementedError('Board.show')
        print('  \u250c'+'\u2500'*6*self.width+'\u2510')
        for n in range(self.height,0,-1):
            line = ('\u2588'*6 + '\u2591'*6 ) * self.width
            if n % 2 > 0:
                line = line[6:]
            line = line[:self.width*6]
            line1 = '  \u2502'+ line + '\u2502'
            line2 = f'{n:2d}\u2502' + line + f'\u2502{n:2d}'
            print(line1)
            print(line2)
            print(line1)
        print('  \u2514'+'\u2500'*6*self.width + '\u2518')
        print('     '+(' '*5).join(alpha))

if __name__ == '__main__':
    x = Board(8)
    x.show()
