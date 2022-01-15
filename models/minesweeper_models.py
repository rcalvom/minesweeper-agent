"""Minesweeper models"""


class BoardState():
    """Board State"""

    def __init__(self, board):
        """Contructor"""
        self.board = board
        self.width = len(board)
        self.height = len(board[0])

    def get_unflaged_mined_cells(self):
        result = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], UncoveredCellState):
                    if self.get_number_of_uncover_neighbours(i, j) == self.board[i][j].number:
                        result.append((i, j))
                elif isinstance(self.board[i][j], CoveredCellState):
                    None
        return result

    def aget_unflaged_mined_cells(self):
        result = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], UncoveredCellState):
                    if self.get_number_of_uncover_neighbours(i, j) == self.board[i][j].number:
                        result.append((i, j))
        return result

    def get_number_of_uncover_neighbours(self, x, y):
        count = 0
        for i in range(x - 1, x + 1):
            for j in range(y - 1, y + 1):
                if i == j:
                    continue
                if i < 0 or i >= self.width:
                    continue
                if j < 0 or j >= self.height:
                    continue
                if isinstance(self.board, CoveredCellState):
                    count += 1
        return count

    def get_covered_cells(self):
        results = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], CoveredCellState):
                    results.append((i, j))
        print(results)
        print(len(results))
        return results
                    


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
        