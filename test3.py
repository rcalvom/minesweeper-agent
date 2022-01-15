"""Test 3 - Agent
This Agent solve minesweeper
"""

# Minesweeper Agent
from agent.risk_minsweeper_agent import RiskMinsweeperAgent

# Matplotlib
import matplotlib.pyplot as plt

# NumPy
import numpy as np

# Pandas
import pandas as pd

mines_factor = [0.05, 0.10]
results_wins = []
results_losses = []
xlabel_mines_factor = []
games = 2

for mine_factor in mines_factor:
    games_won = 0
    agent = RiskMinsweeperAgent(9,9,mine_factor)
    for i in range(games):
        agent.run()
        if agent.is_won:
            games_won += 1
    results_wins.append(games_won)
    results_losses.append(games - games_won)
    xlabel_mines_factor.append('{}%'.format(mine_factor*100))
    print("MINE FACTOR: {}".format(mine_factor))
    print("WINS: {}".format(games_won))
    print("LOSSES: {}".format(games - games_won))
    agent.page.close()


df = pd.DataFrame({
    'Mines density': xlabel_mines_factor,
    'Wins': results_wins,
    'Losses': results_losses
})

df.plot(x="Mines density", y=['Wins', 'Losses'], kind='bar')
plt.show()
