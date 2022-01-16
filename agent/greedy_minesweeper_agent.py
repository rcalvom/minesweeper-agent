"""Greedy Minesweeper Agent"""

# Minesweeper Agent
from unicodedata import numeric
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage

# Utilities
from time import sleep
from random import choice, randint


class GreedyMinesweeperAgent(Agent):

    def __init__(self):
        self.x = int
        self.y = int
        self.mine_factor = numeric
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
            state = self.page.get_board_state()
            list = state.get_unchecked_unflaged_numbers()
            if len(list) == 0:
                cells = state.get_covered_cells()
                cell = choice(cells)
                self.page.uncover_cell(cell[0], cell[1])
            else:
                cells = state.get_unflaged_neighbours(list)
                for cell in cells:
                    self.page.flag_cell(cell[0], cell[1])
                while True:
                    state = self.page.get_board_state()
                    numbers_to_click = state.get_clickable_numbers()
                    for item in numbers_to_click:
                        self.page.click_number(item[0], item[1])
                    if len(numbers_to_click) == 0:
                        break
                

        if self.page.is_lost():
            self.is_won = False
        elif self.page.is_won():
            self.is_won = True
            self._3BV = self.page.get_3BV()
            self.clicks = self.page.get_clicks()
        

    