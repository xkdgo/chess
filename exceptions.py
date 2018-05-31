# -*- coding: utf-8 -*-

class ChessPlayError(Exception):
    pass

class InvalidMove(ChessPlayError):
    pass


class InvalidPosition(ChessPlayError):
    pass


class PositionOccupied(ChessPlayError):
    pass
