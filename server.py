# -*- coding: utf-8 -*-

import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler
from Board import Board
from exceptions import ChessPlayError


class ChessServer(HTTPServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__colors = ['w', 'b']
        self.__turn = 'w'
        self.__currentboard = Board(8)
        self.__currentboard.initialize()

    @property
    def board(self):
        return self.__currentboard

    @property
    def turn(self):
        return self.__turn

    def switch_turn(self):
        if self.__turn == 'b':
            self.__turn = 'w'
        else:
            self.__turn = 'b'

    def request_color(self):
        return self.__colors.pop(0)


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # обрабатывает функцию handshake() от ChessClient
        try:
            color = self.server.request_color()
            # вызываем метод ChessServer и записываем в переменную
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(color.encode('utf-8'))
            # Передаем клиенту переменную color
        except IndexError:
            # если цвета w и b в списке экземпляра закончились
            # то вызываем ошибку доступ запрещен
            self.send_error(403)

    def do_POST(self):
        print(self.path)
        count_of_bytes = int(self.headers['Content-Length'])
        # количество байт которые послал клиент POST запросом
        cmd = self.rfile.read(count_of_bytes).decode('utf-8')
        # cmd -- либо turn либо getpos либо запись хода
        # принимается от клиента методом POST
        print(cmd)
        if cmd == 'turn':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(self.server.turn.encode('utf-8'))
            # при помощи wfile передаем клиенту результат запроса свойства turn
        elif cmd == 'getpos':
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            with self.server.board as brd:
                pickle.dump(brd, self.wfile)
                # передаем клиенту объект python который библиотека
                # pickle преобразует в байты
        else:
            try:
                self.server.board.move(cmd)
                self.server.switch_turn()
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('True'.encode('utf-8'))
            except ChessPlayError:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('False'.encode('utf-8'))

srv = ChessServer(('', 8000), Handler)
srv.serve_forever()



