"""Greedy Minesweeper Agent"""

# Minesweeper Agent
from unicodedata import numeric
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage
from models.minesweeper_models import *

# Utilities
from time import sleep
from random import choice, randint
import numpy as np


class hybrid_minesweeper_agent(Agent):

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
                nextMoves = self.calculateRisk(self.x, self.y)
                randIndex = randint(0, len(nextMoves) - 1)
                nextMove = nextMoves[randIndex]
                self.page.uncover_cell(nextMove[0], nextMove[1])
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

    def calculateRisk(self, rows, columns) -> list:
        
        boardString = self.page.get_board_state().board
        riskMap = np.full((rows,columns), 100)
        boardWarnings = []
        newCoveredCells = []

        for i in range(rows):
            fixedList = []
            for y in range(columns):
                if(isinstance(boardString[i][y], UncoveredCellState)):
                    if((int(boardString[i][y].number) != 0)):
                        fixedList.append(int(boardString[i][y].number))
                    else: fixedList.append(int(9))
                else:
                    fixedList.append(0)
                    newCoveredCells.append((i,y))

            boardWarnings.append(fixedList)

        for indexes in newCoveredCells:
            v = indexes[0]
            w = indexes[1]
            if((v > 0 and w > 0) and (v < (columns - 1) and w < (columns - 1))):
                riskMap[v][w] = boardWarnings[v-1][w-1]+ boardWarnings[v-1][w] + boardWarnings[v-1][w+1] + boardWarnings[v][w-1] + boardWarnings[v][w+1] + boardWarnings[v+1][w-1] + boardWarnings[v+1][w] + boardWarnings[v+1][w+1]
            elif(v == 0 and w == 0):
                riskMap[v][w] = boardWarnings[v][w+1] + boardWarnings[v+1][w] + boardWarnings[v+1][w+1]
            elif(v == (rows - 1) and w == (columns - 1)):
                riskMap[v][w] = boardWarnings[v-1][w-1] +boardWarnings[v-1][w] + boardWarnings[v][w-1]
            elif(v == 0 and w > 0):
                riskMap[v][w] = boardWarnings[v][w-1] + boardWarnings[v+1][w] + boardWarnings[v+1][w-1]
                if(w != (columns - 1)):
                    riskMap[v][w] += boardWarnings[v][w+1] + boardWarnings[v+1][w+1]
            elif(v == (rows - 1) and w > 0):
                riskMap[v][w] = boardWarnings[v-1][w] + boardWarnings[v-1][w+1] + boardWarnings[v][w+1] + boardWarnings[v-1][w-1] + boardWarnings[v][w-1]
            elif(v == (rows - 1) and w == 0):
                riskMap[v][w] = boardWarnings[v-1][w] + boardWarnings[v-1][w+1] + boardWarnings[v][w+1]
            elif((v > 0 and v < (rows - 1)) and w == 0):
                riskMap[v][w] = boardWarnings[v-1][w] + boardWarnings[v-1][w+1] + boardWarnings[v][w+1] + boardWarnings[v+1][w] + boardWarnings[v+1][w+1]
            elif((v > 0 and v < (rows - 1)) and w == (columns - 1)):
                riskMap[v][w] = boardWarnings[v-1][w-1] + boardWarnings[v-1][w] + boardWarnings[v][w-1] + boardWarnings[v+1][w-1] + boardWarnings[v+1][w]

        lowestNumber = np.amin(riskMap)
        possibleIndexes = np.where(riskMap == lowestNumber)
        listOfCoordinates = list(zip(possibleIndexes[0], possibleIndexes[1]))

        return listOfCoordinates
        

    