"""Random Minesweeper Agent"""

# Minesweeper Agent
from random import randint
from time import sleep
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage

class RandomMinesweeperAgent(Agent):

    def __init__(self, mine_factor):
        self.mine_factor = mine_factor
        self.page = MinesweeperPage()
        self.is_won = bool
        self._3BV = int
        self.clicks = int

    def run(self):
        self.page.navigate_to_minesweeper_website()
        self.page.create_game()
        self.page.select_custom_difficulty_level(9, 9, int(9 * 9 * self.mine_factor))
        sleep(1)
        while not self.page.is_lost() and not self.page.is_won():
            self.page.uncover_cell(randint(0, 8), randint(0, 8))

        if self.page.is_lost():
            self.is_won = False
        elif self.page.is_won():
            self.is_won = True
            #self._3BV = self.page.get_3BV()
            #self.clicks = self.page.get_clicks()


        

    