"""Greedy Minesweeper Agent"""

# Minesweeper Agent
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage

# Utilities
from time import sleep
from random import choice, randint

class GreedyMinesweeperAgent(Agent):

    def __init__(self, x, y, mine_factor):
        self.x = x
        self.y = y
        self.mine_factor = mine_factor
        self.page = MinesweeperPage()
        self.is_won = bool
        self._3BV = int
        self.clicks = int

    def run(self):
        self.page.navigate_to_minesweeper_website()
        self.page.create_game()
        self.page.select_custom_difficulty_level(self.x, self.y, int(self.x * self.y * self.mine_factor))
        sleep(1)
        self.page.uncover_cell(randint(0, self.x - 1), randint(0, self.y - 1))
        while not self.page.is_lost() and not self.page.is_won():
            list = self.page.get_board_state().get_unflaged_mined_cells()
            if len(list) == 0:
                cell = choice(self.get_covered_cells())
                self.page.uncover_cell(cell[0], cell[1])
            else:
                for item in list:
                    self.page.uncover_cell(item[0], item[1])

        if self.page.is_lost():
            self.is_won = False
        elif self.page.is_won():
            self.is_won = True
            #self._3BV = self.page.get_3BV()
            #self.clicks = self.page.get_clicks()

    def get_covered_cells(self) -> list:
        cells = self.page.get_board_state().get_covered_cells()
        for cell in cells:
            self.page.uncover_cell(cell[0], cell[1])
        

    