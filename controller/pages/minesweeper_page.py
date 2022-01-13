"""Minesweeper Page"""


# Minesweeper Agent
from controller.pages.base_page import BasePage
from models.minesweeper_models import BoardState, CoveredCellState, UncoveredCellState

# Utilities
import re


class MinesweeperPage(BasePage):
    """Minesweeper Selenium Page"""

    def __init__(self):
        """Constructor"""
        super().__init__(10.0)

    def navigate_to_minesweeper_website(self):
        """Navigate to minesweeper website"""
        super().open_url("https://minesweeper.online")
    
    def create_game(self):
        """Create a new game"""
        super().click_element("/html/body/div[3]/div[2]/div/div[1]/div[1]/div/ul[1]/li[1]/a/span")

    def select_beginner_difficulty_level(self):
        """Select a beginner difficulty level"""
        super().click_element("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[13]/div/div[1]/a[1]/span")

    def select_intermediate_difficulty_level(self):
        """Select a intermediate difficulty level"""
        super().click_element("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[13]/div/div[1]/a[2]/span")

    def select_expert_difficulty_level(self):
        """Select a expert difficulty level"""
        super().click_element("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[13]/div/div[1]/a[3]/span")

    def select_custom_difficulty_level(self, width, height, mines):
        """Select a custom difficulty level"""
        super().click_element("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[13]/div/div[1]/a[4]/span")
        super().write("//*[@id='custom_width']", str(width))
        super().write("//*[@id='custom_height']", str(height))
        super().write("//*[@id='custom_mines']", str(mines))
        super().click_element("//*[@id='level_update_btn']")

    def uncover_cell(self, x, y):
        """Click an specific game cell in (x, y) position"""
        super().click_element("//div[@id='cell_{0}_{1}']".format(x, y))

    def flag_cell(self, x, y):
        """Flag an specific game cell in (x, y) position"""
        super().right_click_element("//div[@id='cell_{0}_{1}']".format(x, y))    

    def get_board_state(self) -> BoardState:
        """Return the current Board State"""
        cells_html = super().find("//*[@id='A43']").get_attribute("innerHTML")
        cells_regex = re.findall(r"<div (.+?)></div>", cells_html)
        cells = []
        for cell_regex in cells_regex:
            if "clear" not in cell_regex:
                cells.append(cell_regex)
        data = {}
        x_last = int(re.match(r".*data-x=\"(.+?)\".*", cells[-1]).group(1)) + 1
        y_last = int(re.match(r".*data-y=\"(.+?)\".*", cells[-1]).group(1)) + 1
        for i in range(x_last):
            data[i] = {}
            for j in range(y_last):
                data[i][j] = None
        for index, cell in enumerate(cells):
            element_class = re.match(r".*class=\"(.+?)\".*", cell).group(1)
            if "hd_opened" in element_class:
                data[index // x_last][index % x_last] = UncoveredCellState(number=re.match(r".*hd_type(\d+).*", element_class).group(1))
            elif "hd_closed" in element_class:
                data[index // x_last][index % x_last] = CoveredCellState(flaged="hd_flag" in element_class)
        return BoardState(board=data)
            

    