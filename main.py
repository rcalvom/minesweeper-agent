"""Main method"""

# Minesweeper Agent
from controller.pages.minesweeper_page import MinesweeperPage

page = MinesweeperPage()

page.navigate_to_minesweeper_website()
page.create_game()
page.select_beginner_difficulty_level()
page.flag_cell(2, 2)
page.uncover_cell(5, 5)
print(str(page.get_board_state().board))
page.close()