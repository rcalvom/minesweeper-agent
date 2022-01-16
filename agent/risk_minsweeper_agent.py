# Minesweeper Agent
from agent.agent import Agent
from controller.pages.minesweeper_page import MinesweeperPage
from models.minesweeper_models import *

# Utilities
from time import sleep
from random import randint
import numpy as np


class RiskMinsweeperAgent(Agent):

    def __init__(self):
        self.x = int
        self.y = int
        self.mine_factor = int
        self.page = MinesweeperPage()
        self.is_won = bool
        self._3BV = int
        self.clicks = int
        self.possible = UncoveredCellState(0)

    def run(self):
        self.page.navigate_to_minesweeper_website()
        self.page.create_game()
        self.page.select_custom_difficulty_level(self.x, self.y, int(self.x * self.y * self.mine_factor))
        sleep(1)

        while not self.page.is_lost() and not self.page.is_won():
            nextMoves = self.calculateRisk(self.x, self.y)
            bla = randint(0, len(nextMoves)-1)
            nextMove = nextMoves[bla]
            self.page.uncover_cell(nextMove[0], nextMove[1])

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
                if(isinstance(boardString[i][y], type(self.possible))):
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
        