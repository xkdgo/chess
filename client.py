# -*- coding: utf-8 -*-

from urllib.request import urlopen
import time
import pickle
from Board import Board


class ChessClient(object):
    # обслуживающий класс
    def __init__(self, host, port=8000):
        self.__host = host
        self.__port = port

    @property
    def url(self):
        try:
            return 'http://{0}:{1}/{2}'.format(
                self.__host, self.__port, self.color)
        except AttributeError:
            return 'http://{0}:{1}'.format(
                self.__host, self.__port)

    @property
    def color(self):
        return self.__color

    def handshake(self):
        # Первое подключние -- определяем цвет фигур
        # функция выставляет переменную self.__color
        with urlopen(self.url) as response:
            self.__color = response.read(1024).decode('utf-8')

    @property
    def turn(self):
        # функция которая возвращает кому пора ходить
        with urlopen(self.url, data='turn'.encode('utf-8')) as resp:
            return resp.read(1024).decode('utf-8')

    def wait(self):
        # функция периодически проверяет чей ход и если чужой
        # то пауза
        while self.turn != self.color:
            time.sleep(2.0)

    def request_board(self):
        # функция запрашивает доску с позицией фигур
        with urlopen(self.url, data='getpos'.encode('utf-8')) as brd_bytes:
            result = pickle.load(brd_bytes)
            # восстанавливаем доску при помощи pickle
            # декодируем объект python
        result.restore_for_pickle()
        return result

    def move(self, text):
        with urlopen(self.url, data=text.encode('utf-8')) as resp:
            return resp.read(1024).decode('utf-8') == 'True'


"""
host = '127.0.0.1'
port = 8000
url = 'http://{}:{}'.format(host, port)
вместо этих переменных создали вспомогательный класс ChessClient
определенный ранее
"""

client = ChessClient('localhost')
client.handshake()
# print(client.color)
# print(client.turn)
# brd = client.request_board()
# brd.show()
# client.wait()
# client.move('pe2-e3')
# client.request_board().show()

while True:
    client.wait()
    client.request_board().show()
    while True:
        move_text = input('{}: '.format(client.color))
        if client.move(move_text):
            break
        print('Invalid move, try again')
    client.request_board().show()





