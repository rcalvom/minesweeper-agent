"""Minesweeper models"""


class BoardState():
    """Board State"""

    def __init__(self, board):
        """Contructor"""
        self.board = board


class BaseCellState():
    """Base Cell State"""
    pass


class UncoveredCellState(BaseCellState):
    """Uncovered Cell State"""

    def __init__(self, number):
        """Constructor"""
        self.number = number


class CoveredCellState(BaseCellState):
    """Covered Cell State"""

    def __init__(self, flaged):
        """Contructor"""
        self.flaged = flaged
        