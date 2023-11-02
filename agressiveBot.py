from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState
from schnapsen.deck import Suit, Card, Rank
from typing import Optional
import random



class AgressiveBot(Bot):
    def get_move(self, state: 'PlayerPerspective', leader_move: Optional['Move']) -> 'Move':
        
        trumpSuit = state.get_trump_suit()
        valid_moves = state.valid_moves()
        
        move = AgressiveBot.agressive_move(state, leader_move, valid_moves, trumpSuit)

        return move
        
        



    def agressive_move(state, leader_move, valid_moves, trumpSuit):

        #If Leader:
        #If you have trump cards, play highest trump suit
        #Else play highest card (#Play same suit you played before)

        #If Follower:
        #If you have trump cards and leader doesnt play trump, then play lowest trump card
        #Elif you have same suit then play the highest same suit as opponent

        marriageList = []
        trumpExchangeList = []
        trumpMoveList = []
        nonTrumpMoveList = []
        sameSuitList = []
        nonSameSuitNonTrumpList = []
    
        oldScore = 0 

        #early in game:
        #better to lead a non trump jack,
        #or if youve seen its marriage partner played, lead non trump queen or king
       

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
                for move in marriageList:
                    return move
            
            elif len(trumpMoveList) != 0:                                   #play lowest ranking trump card
                for move in trumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score > oldScore:
                        oldScore = score
                        highestRankingCard = move
                return highestRankingCard
            
            elif len(nonTrumpMoveList) != 0:
                for move in nonTrumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score > oldScore:
                        oldScore = score
                        highestRankingCard = move
                return highestRankingCard

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
            
            if len(trumpMoveList) != 0:                                   #play lowest ranking trump card
                for move in trumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score > oldScore:
                        oldScore = score
                        highestRankingCard = move
                return highestRankingCard

            elif len(sameSuitList) != 0:                                #play lowest ranking same suit card
                for move in sameSuitList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score > oldScore:
                        oldScore = score
                        highestRankingCard = move
                return highestRankingCard
            
            elif len(nonSameSuitNonTrumpList) != 0:
                oldScore = 100                                #play lowest ranking non trump card
                for move in nonSameSuitNonTrumpList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score < oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard
        
            else:
                choice = random.choice(valid_moves)
                return choice

