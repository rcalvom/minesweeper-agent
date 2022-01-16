"""Random Minesweeper Agent"""

# Minesweeper Agent
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage

# Utilities
from random import choice
from time import sleep

class RandomMinesweeperAgent(Agent):

    def __init__(self):
        self.x = int
        self.y = int
        self.mine_factor = int
        self.page = MinesweeperPage()
        self.is_won = bool
        self._3BV = int
        self.clicks = int

    def run(self):
        self.page.navigate_to_minesweeper_website()
        self.page.create_game()
        self.page.select_custom_difficulty_level(self.x, self.y, int(self.x * self.y * self.mine_factor))
        sleep(1)
        while not self.page.is_lost() and not self.page.is_won():
            state = self.page.get_board_state()
            cells = state.get_covered_cells()
            cell = choice(cells)
            self.page.uncover_cell(cell[0], cell[1])

        if self.page.is_lost():
            self.is_won = False
        elif self.page.is_won():
            self.is_won = True
            self._3BV = self.page.get_3BV()
            self.clicks = self.page.get_clicks()


        

    