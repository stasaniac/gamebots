from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState
from schnapsen.deck import Suit, Card, Rank
from schnapsen.tournament import tournament
from schnapsen.bots import HandValueBot
from schnapsen.bots import RandBot
from schnapsen.bots import PassiveBot
from schnapsen.bots import agressiveBot
from schnapsen.bots import RdeepBot
from typing import Optional
import numpy as np
import random
import matplotlib.pyplot as plt


#### HandValueBot ####



def HeuristicFinderHandValue(bot2):
    #heuristicValues = np.arange(0,10.1,0.1)
    heuristicValuess = [0,0,0,
                                0.1,0.1,0.1,
                                0.2,0.2,0.2,
                                0.3,0.3,0.3,
                                0.4,0.4,0.4,
                                0.5,0.5,0.5,
                                0.6,0.6,0.6,
                                0.7,0.7,0.7,
                                0.8,0.8,0.8,
                                0.9,0.9,0.9,
                                1.0,1.0,1.0]
    heuristicValues = np.array(heuristicValuess)

    winsCount = []
    for point in heuristicValues:
        winsCount.append(tournament(HandValueBot(point),bot2))
        

    winsCount = np.array(winsCount)

    idx = np.argsort(winsCount)  

    heuristicValues = heuristicValues[idx]
    winsCount = winsCount[idx]

    x = np.flip(heuristicValues)
    y = np.flip(winsCount)
    #print(np.flip(heuristicValues))
    #print(np.flip(winsCount))

    return x,y


heuristicValues = []
winsCount = []

bot2 = RdeepBot(num_samples = 8,depth = 4,rand = random.Random(42))


# point = 2.0
# print(tournament(HandValueBot(point),bot2))

x,y = HeuristicFinderHandValue(bot2)
plt.plot(x,y,'ro')
plt.xlabel('Hand Strength Threshold')
plt.ylabel('Number of Wins / 1000')
plt.show()



print(y[:10])

#

#calculate hand value, as game progresses
print(x)
print(y)


def ExperimentPassiveBot(bot2):
    heuristicValues = np.arange(0,5.1,0.1)
    #print(heuristicValues)

    winsCount = []
    
    winsCount.append(tournament(PassiveBot(),bot2))
    #np.append(winsCount, tournament(HandValueBot(point),bot2))
        

    winsCount = np.array(winsCount)

    idx = np.argsort(winsCount)  

    heuristicValues = heuristicValues[idx]
    winsCount = winsCount[idx]

    x = np.flip(heuristicValues)
    y = np.flip(winsCount)
    #print(np.flip(heuristicValues))
    #print(np.flip(winsCount))

    return x,y


#tournament(PassiveBot(),bot2)
        




        







        
