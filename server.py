# -*- coding: utf-8 -*-

import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler
from Board import Board


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

    def request_color(self):
        return self.__colors.pop(0)


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # обрабатывает функцию handshake() от ChessClient
        try:
            color = self.server.request_color()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(color.encode('utf-8'))
        except IndexError:
            self.send_error(403)

    def do_POST(self):
        print(self.path)
        count = int(self.headers['Content-Length'])
        # количество байт которые послал клиент POST запросом
        cmd = self.rfile.read(count).decode('utf-8')
        # cmd -- либо turn либо getpos либо запись хода
        print(cmd)
        if cmd == 'turn':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(self.server.turn.encode('utf-8'))
        elif cmd == 'getpos':
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            pickle.dump(self.server.board, self.wfile)
            # передаем клиенту объект python который библиотека
            # pickle преобразует в байты
        else:
            self.send_error(404)

srv = ChessServer(('', 8000), Handler)
srv.serve_forever()



