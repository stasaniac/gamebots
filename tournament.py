from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState
from schnapsen.deck import Suit, Card, Rank
from typing import Optional
import random
import pathlib
import numpy as np

import click
from schnapsen.bots import MLDataBot, train_ML_model, MLPlayingBot, RandBot, PassiveBot, AgressiveBot, HandValueBot

from schnapsen.bots.example_bot import ExampleBot

from schnapsen.game import (Bot, Move, PlayerPerspective,
                            SchnapsenGamePlayEngine, Trump_Exchange)
from schnapsen.twenty_four_card_schnapsen import \
    TwentyFourSchnapsenGamePlayEngine

from schnapsen.bots.rdeep import RdeepBot
import matplotlib.pyplot as plt

def play_games_and_return_stats(engine: SchnapsenGamePlayEngine, bot1: Bot, bot2: Bot, number_of_games: int) -> int:
    """
    Play number_of_games games between bot1 and bot2, using the SchnapsenGamePlayEngine, and return how often bot1 won.
    Prints progress.
    """
    bot1_wins: int = 0
    lead, follower = bot1, bot2
    for i in range(1, number_of_games + 1):
        if i % 2 == 0:
            # swap bots so both start the same number of times
            lead, follower = follower, lead
        winner, _, _ = engine.play_game(lead, follower, random.Random(i))
        if winner == bot1:
            bot1_wins += 1
        if i % 500 == 0:
            print(f"Progress: {i}/{number_of_games}")
    return bot1_wins

def tournament(bot1,bot2):
    engine = SchnapsenGamePlayEngine()
    bot1_wins = play_games_and_return_stats(engine, bot1, bot2, 1000)
    #print(bot1_wins)
    return bot1_wins





