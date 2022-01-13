"""Minesweeper Agent"""

# Minesweeper Agent
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage

class MinesweeperAgent(Agent):

    def __init__(self, board):
        self.board = board
        self.page = MinesweeperPage()

    def uncover_cell(self, x, y):
        self.page.uncover_cell(x, y)


    def run(self):
        #TODO: EJECUCION DEL BOT

        cells = []

        for cell in cells: #TODO: CELLS
            self.uncover_cell(cell.x, cell.y)


        

    