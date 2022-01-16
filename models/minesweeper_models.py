"""Minesweeper models"""


class BoardState():
    """Board State"""

    def __init__(self, board):
        """Contructor"""
        self.board = board
        self.width = len(board)
        self.height = len(board[0])

    def get_unchecked_unflaged_numbers(self) -> list:
        result = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], UncoveredCellState):
                    if self.get_number_of_uncover_neighbours(i, j) == self.board[i][j].number:
                        result.append((i, j))
                elif isinstance(self.board[i][j], CoveredCellState):
                    None
        return result

    def get_unflaged_neighbours(self, list) -> set:
        result = set()
        for item in list:
            for i in range(item[0] - 1, item[0] + 2):
                for j in range(item[1] - 1, item[1] + 2):
                    if i == item[0] and j == item[1]:
                        continue
                    if i < 0 or i >= self.width:
                        continue
                    if j < 0 or j >= self.height:
                        continue
                    if isinstance(self.board[i][j], CoveredCellState):
                        if not self.board[i][j].flaged:
                            result.add((i, j))
        return result

    def get_clickable_numbers(self) -> set:
        result = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], UncoveredCellState):
                    if self.board[i][j].number != 0:
                        if self.is_clickable_number(i, j, self.board[i][j].number):
                            result.append((i, j))                    
        return result

    def is_clickable_number(self, x, y, number) -> bool:
        count = 0
        has_unflaged = False
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if i < 0 or i >= self.width:
                    continue
                if j < 0 or j >= self.height:
                    continue
                if isinstance(self.board[i][j], CoveredCellState) and self.board[i][j].flaged:
                    count += 1
                if isinstance(self.board[i][j], CoveredCellState) and not self.board[i][j].flaged:
                    has_unflaged = True
        return count == number and has_unflaged

    def get_number_of_cover_neighbours(self, x, y):
        count = 0
        has_unflagged = False
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if i < 0 or i >= self.width:
                    continue
                if j < 0 or j >= self.height:
                    continue
                if isinstance(self.board[i][j], CoveredCellState):
                    count += 1
                    has_unflagged |= not self.board[i][j].flaged
        return count if has_unflagged else -1

    def get_covered_cells(self):
        results = []
        for i in range(self.width):
            for j in range(self.height):
                if isinstance(self.board[i][j], CoveredCellState) and not self.board[i][j].flaged:
                    results.append((i, j))
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
        