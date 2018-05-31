# -*- coding: utf-8 -*-

from urllib.request import urlopen
import time


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
        while self.turn != self.color:
            time.sleep(2.0)


"""
host = '127.0.0.1'
port = 8000
url = 'http://{}:{}'.format(host, port)
вместо этих переменных создали вспомогательный класс ChessClient
определенный ранее
"""

client = ChessClient('localhost')
client.handshake()
print(client.color)
