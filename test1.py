"""
Test 1 - Agent
This Agent solve minesweeper randomly
"""

# Minesweeper Agent
from agent.random_minesweeper_agent import RandomMinesweeperAgent

# Pandas
import pandas as pd

sizes = [(10, 10), (12, 12), (14, 14), (16, 16), (18, 18)]
mines_proportions = [0.05, 0.10, 0.15, 0.20, 0.25]
games = 50

df = pd.DataFrame(columns=[
    "TEST",
    "WIDTH",
    "HEIGHT",
    "MINES_PROPORTION",
    "VICTORY",
    "CLICKS",
    "3BV",
    "EFICIENCY"
])

agent = RandomMinesweeperAgent()
for size in sizes:
    for mines_proportion in mines_proportions:
        agent.x = size[0]
        agent.y = size[1]
        agent.mine_factor = mines_proportion
        for i in range(games):
            agent.run()
            if agent.is_won:
                data = {
                    "TEST": (i + 1),
                    "WIDTH": size[0],
                    "HEIGHT": size[1],
                    "MINES_PROPORTION": mines_proportion,
                    "VICTORY": True,
                    "CLICKS": agent.clicks,
                    "3BV": agent._3BV,
                    "EFICIENCY": agent._3BV / agent.clicks
                }
                df = df.append(data, ignore_index=True)
            else:
                data = {
                    "TEST": (i + 1),
                    "WIDTH": size[0],
                    "HEIGHT": size[1],
                    "MINES_PROPORTION": mines_proportion,
                    "VICTORY": False,
                    "CLICKS": None,
                    "3BV": None,
                    "EFICIENCY": None
                }
                df = df.append(data, ignore_index=True)
agent.page.close()

df.to_excel("test1.xlsx")


