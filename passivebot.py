
from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState
from schnapsen.deck import Suit, Card, Rank
from typing import Optional
import random



class PassiveBot(Bot):


    def __init__(self) -> None:
        super().__init__()

    def get_move(self, state: 'PlayerPerspective', leader_move: Optional['Move']) -> 'Move':

        valid_moves = state.valid_moves()
        trumpSuit = state.get_trump_suit()
        oldScore = 100   

        marriageList = []
        trumpExchangeList = []

        #print(valid_moves)
        for move in valid_moves:
            if move.is_marriage():
                marriageList.append(move) 
            elif move.is_trump_exchange():           #check for trump exchange move
                trumpExchangeList.append(move)
            else: 
                score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                if score <= oldScore:
                    oldScore = score
                    lowestRankingCard = move
        #print(lowestRankingCard)

        move = PassiveBot.passive_move(state, leader_move, valid_moves, trumpSuit)


        return move

        


    def passive_move(state, leader_move, valid_moves, trumpSuit):

        marriageList = []
        trumpExchangeList = []
        trumpMoveList = []
        nonTrumpMoveList = []
        sameSuitList = []
        nonSameSuitNonTrumpList = []
    

        oldScore = 100      

        #early in game:
        #better to lead a non trump jack,
        #or if youve seen its marriage partner played, lead non trump queen or king
       

        
        #print(trumpMoveList)
        #print(nonTrumpMoveList)

        if state.am_i_leader() == True:

            for move in valid_moves:
                
                if move.is_marriage():
                    marriageList.append(move) 
                elif move.is_trump_exchange():           #check for trump exchange move
                    trumpExchangeList.append(move)       
                elif move.card.suit == trumpSuit:     #check for trump move cards
                    trumpMoveList.append(move)
                else:                                      
                    nonTrumpMoveList.append(move)

            if len(trumpExchangeList) != 0:
                #print("Length TrumpExchangeList not 0")
                for move in trumpExchangeList:
                    return move

            elif len(marriageList) != 0:
                #print("Length marriageList not 0") 
                for move in marriageList:
                    return move
            
            elif len(nonTrumpMoveList) != 0:
                #print("Length nonTrumpMoveList not 0") 
                for move in nonTrumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard

            elif len(trumpMoveList) != 0:                                   #play lowest ranking trump card
                #print("Length trumpMoveList is not 0")
                for move in trumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard

            else:
                choice = random.choice(valid_moves)
                return choice


            

        else:
            for move in valid_moves:

                if move.is_marriage():
                    marriageList.append(move)
                elif move.is_trump_exchange():           #check for trump exchange move
                    trumpExchangeList.append(move)             
                elif leader_move.is_marriage() == False and move.card.suit == leader_move.card.suit: 
                    sameSuitList.append(move)
                elif move.card.suit == trumpSuit:                                  #check for trump move cards
                    trumpMoveList.append(move)
                else:
                    nonSameSuitNonTrumpList.append(move)

            if len(sameSuitList) != 0:                                #play lowest ranking same suit card
                #print("Length sameSuitList not 0")
                for move in sameSuitList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard
            
            if len(nonSameSuitNonTrumpList) != 0:                                #play lowest ranking non trump card
                #print("Length nonSameSuitNonTrumpList not 0")
                for move in nonSameSuitNonTrumpList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard
        
            elif len(trumpMoveList) != 0:                                   #play lowest ranking trump card
                #print("Length trumpMoveList is not 0")
                for move in trumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard

            else:
                choice = random.choice(valid_moves)
                return choice

        

 
        
                

