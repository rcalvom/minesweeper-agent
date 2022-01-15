"""Main method"""

# Minesweeper Agent
from controller.pages.minesweeper_page import MinesweeperPage
from models.minesweeper_models import *



page = MinesweeperPage()
mModel = UncoveredCellState(0)

page.navigate_to_minesweeper_website()
page.create_game()
page.select_beginner_difficulty_level()
page.flag_cell(2, 2)
page.uncover_cell(5, 5)

boardString = page.get_board_state().board

