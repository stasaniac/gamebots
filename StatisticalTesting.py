from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState
from schnapsen.deck import Suit, Card, Rank
from schnapsen.tournament import tournament
from schnapsen.bots import HandValueBot
from schnapsen.bots import RandBot
from schnapsen.bots import PassiveBot
from schnapsen.bots import AgressiveBot
from schnapsen.bots import RdeepBot
from schnapsen.bots import RandHandStrengthBot
from typing import Optional
import numpy as np
import random
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

print("Number of wins: ")
##### HandValueBot
bot1 = HandValueBot(0.5)
bot2 = RdeepBot(num_samples = 8,depth = 4,rand = random.Random(42))

winsHbot = tournament(bot1, bot2)
print(f"HandValueBot vs Rdeep", winsHbot)

##### Aggressive
bot1 = AgressiveBot()
bot2 = RdeepBot(num_samples = 8,depth = 4,rand = random.Random(42))

winsAggressive = tournament(bot1, bot2)
print(f"Aggressive vs Rdeep", winsAggressive)

##### Passive
bot1 = PassiveBot()
bot2 = RdeepBot(num_samples = 8,depth = 4,rand = random.Random(42))

winsPassive = tournament(bot1, bot2)
print(f"Passive vs Rdeep", winsPassive)

##### HbotRandom
bot1 = RandHandStrengthBot()
bot2 = RdeepBot(num_samples = 8,depth = 4,rand = random.Random(42))

winsHbotRand = tournament(bot1, bot2)
print(f"HbotRand vs Rdeep", winsHbotRand)


print("  ")
print("----------")
print("Testing:")
print("----------")
print("  ")

#### For Hbot vs Aggressive

k1 = winsHbot
k2 = winsAggressive
n1 = 1000
n2 = 1000
zscore, pval = proportions_ztest([k1,k2], [n1,n2])
print("Hbot vs Aggressive")
print(f"Z-score:", zscore)
print(f"pval:", pval)

print("  ")
print("----------")
print("  ")

#### For Hbot vs Passive

k1 = winsHbot
k2 = winsPassive
n1 = 1000
n2 = 1000
zscore, pval = proportions_ztest([k1,k2], [n1,n2])
print("Hbot vs Passive")
print(f"Z-score:", zscore)
print(f"pval:", pval)

print("  ")
print("----------")
print("  ")

#### For Hbot vs HbotRandom

k1 = winsHbot
k2 = winsHbotRand
n1 = 1000
n2 = 1000
zscore, pval = proportions_ztest([k1,k2], [n1,n2])
print("Hbot vs HbotRand")
print(f"Z-score:", zscore)
print(f"pval:", pval)

print("  ")
print("----------")
print("  ")


#### For HbotRandom vs Aggressive

k1 = winsHbotRand
k2 = winsAggressive
n1 = 1000
n2 = 1000
zscore, pval = proportions_ztest([k1,k2], [n1,n2])
print("HbotRandom vs Aggressive")
print(f"Z-score:", zscore)
print(f"pval:", pval)

print("  ")
print("----------")
print("  ")

#### For HbotRandom vs Passive

k1 = winsHbotRand
k2 = winsPassive
n1 = 1000
n2 = 1000
zscore, pval = proportions_ztest([k1,k2], [n1,n2])
print("HbotRandom vs Passive")
print(f"Z-score:", zscore)
print(f"pval:", pval)

print("  ")
print("----------")
print("  ")


botList = ['Hbot', 'Pbot','Abot','randomHbot']
botWins = [300,303, 313, 315,315]

colors = ['white','green', 'blue', 'purple', 'brown', 'teal','white']
plt.bar(botList, botWins, color=colors)
plt.title('Bot Wins vs Rdeep', fontsize=14)
plt.xlabel('Bot Name', fontsize=14)
plt.ylabel('Bot Wins', fontsize=14)
plt.ylim(max(botWins), min(botWins))
plt.gca().invert_yaxis()
plt.show()