from schnapsen.game import Bot, PlayerPerspective, Move, SchnapsenTrickScorer, Talon, Previous, GameState, SchnapsenDeckGenerator, GamePhase
from schnapsen.deck import Suit, Card, Rank
from typing import Optional
import random



class HandValueBot(Bot):


    def __init__(self, threshold) -> None:
        super().__init__()
        self.threshold = threshold

    def get_move(self, state: 'PlayerPerspective', leader_move: Optional['Move']) -> 'Move':

        valid_moves = state.valid_moves()
        trumpSuit = state.get_trump_suit()

        threshold = self.threshold
        
        move = HandValueBot.hand_value_bot(state, leader_move, threshold, valid_moves, trumpSuit)

        return move

        
    def hand_value_bot(state, leader_move, threshold, valid_moves, trumpSuit) -> 'Move':
        hand_value = HandValueBot.probability_value(state, trumpSuit, leader_move)


        if hand_value > threshold:
            move = HandValueBot.agressive_move(state, leader_move, valid_moves, trumpSuit)

        else: 
            move = HandValueBot.passive_move(state, leader_move, valid_moves, trumpSuit) 

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
       

        for move in valid_moves:
                
                if move.is_marriage():
                    marriageList.append(move) 
                elif move.is_trump_exchange():           #check for trump exchange move
                    trumpExchangeList.append(move)       
                elif move.card.suit == trumpSuit:     #check for trump move cards
                    trumpMoveList.append(move)
                else:                                      
                    nonTrumpMoveList.append(move)

        if state.am_i_leader() == True:

            if len(trumpExchangeList) != 0:
                for move in trumpExchangeList:
                    return move

            elif len(marriageList) != 0:
                for move in marriageList:
                    return move
            
            elif len(nonTrumpMoveList) != 0:
                for move in nonTrumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard

            elif len(trumpMoveList) != 0:                                   #play lowest ranking trump card
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
                for move in sameSuitList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard
            
            if len(nonSameSuitNonTrumpList) != 0:                                #play lowest ranking non trump card
                for move in nonSameSuitNonTrumpList:                     
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard
        
            elif len(trumpMoveList) != 0:                                   #play lowest ranking trump card
                for move in trumpMoveList:
                    score = SchnapsenTrickScorer().rank_to_points(move.card.rank)
                    if score <= oldScore:
                        oldScore = score
                        lowestRankingCard = move
                return lowestRankingCard

            else:
                choice = random.choice(valid_moves)
                return choice


    def agressive_move(state, leader_move, valid_moves, trumpSuit):
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
        
    def get_hand_value(state: 'PlayerPerspective', trumpSuit) -> int:
        
        hand = state.get_hand()
        cards = hand.get_cards()
        hand_value = 0

        for card in cards:
            if card.suit == trumpSuit:
                if card.rank == Rank(1):
                    hand_value += 21
                elif card.rank == Rank(10):
                    hand_value += 20
                elif card.rank == Rank(13):
                    hand_value += 14
                elif card.rank == Rank(12):
                    hand_value += 13
                elif card.rank == Rank(11):
                    hand_value += 12
            else:
                if card.rank == Rank(1):
                    hand_value += 11
                elif card.rank == Rank(10):
                    hand_value += 10
                elif card.rank == Rank(13):
                    hand_value += 4
                elif card.rank == Rank(12):
                    hand_value += 3
                elif card.rank == Rank(11):
                    hand_value += 2
        
        return hand_value


    def probability_value(state : 'PlayerPerspective', trumpSuit, leader_move : Optional['Move']):

        hand = state.get_hand()
        hand_cards = hand.get_cards()
        hand_value = 0
        all_cards = SchnapsenDeckGenerator.get_initial_deck(SchnapsenDeckGenerator)
        seen_cards = state.seen_cards(leader_move)


        if state.get_phase() == GamePhase.ONE: 
            if state.am_i_leader() == True:

                for hand_card in hand_cards:
                    hand_card_points = SchnapsenTrickScorer().rank_to_points(hand_card.rank)
                    wins = 0
                    played = 0
                    for opponent_card in all_cards:
                        if opponent_card in seen_cards:
                            continue
                        else:
                            played += 1
                            opponent_card_points = SchnapsenTrickScorer().rank_to_points(opponent_card.rank)
                            if hand_card.suit is opponent_card.suit:
                            # same suit, either trump or not
                                if hand_card_points > opponent_card_points:
                                    wins += 1
                                else:
                                    continue
                            elif hand_card.suit is trumpSuit:
                            # the follower suit cannot be trumps as per the previous condition
                                wins += 1
                            elif opponent_card.suit is trumpSuit:
                            # the leader suit cannot be trumps because of the previous conditions
                                continue
                            else:
                            # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                                wins += 1
                    card_value = (wins/played)
                    hand_value += card_value

                return hand_value

            else: 
                played = 1
                for hand_card in hand_cards:

                    hand_card_points = SchnapsenTrickScorer().rank_to_points(hand_card.rank)
                    wins = 0

                    if leader_move.is_marriage():
                        opponent_card_points = SchnapsenTrickScorer().rank_to_points(leader_move.queen_card.rank)
                        if leader_move.queen_card.suit is hand_card.suit:
                        # same suit, either trump or not
                            if hand_card_points > opponent_card_points:
                                continue
                            else:
                                wins += 1
                        elif hand_card.suit is trumpSuit:
                        # the follower suit cannot be trumps as per the previous condition
                            wins += 1
                        elif leader_move.queen_card.suit is trumpSuit:
                        # the leader suit cannot be trumps because of the previous conditions
                            continue
                        else:
                        # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                            continue
                        

                    else:
                        opponent_card_points = SchnapsenTrickScorer().rank_to_points(leader_move.card.rank)

                        if hand_card.suit is leader_move.card.suit:
                            # same suit, either trump or not
                            if hand_card_points > opponent_card_points:
                                wins += 1
                            else:
                                continue
                        elif hand_card.suit is trumpSuit:
                        # the follower suit cannot be trumps as per the previous condition
                            wins += 1
                        elif leader_move.card.suit is trumpSuit:
                        # the leader suit cannot be trumps because of the previous conditions
                            continue
                        else:
                        # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                            continue
                    
                    card_value = (wins/played)
                    hand_value += card_value

            return hand_value

        else: 
            opponent_hand = state.get_opponent_hand_in_phase_two()
            opponent_cards = opponent_hand.get_cards()
            if state.am_i_leader() == True:

                for hand_card in hand_cards:
                    hand_card_points = SchnapsenTrickScorer().rank_to_points(hand_card.rank)
                    wins = 0
                    played = 0
                    for opponent_card in opponent_cards:
                            played += 1
                            opponent_card_points = SchnapsenTrickScorer().rank_to_points(opponent_card.rank)
                            if hand_card.suit is opponent_card.suit:
                            # same suit, either trump or not
                                if hand_card_points > opponent_card_points:
                                    wins += 1
                                else:
                                    continue
                            elif hand_card.suit is trumpSuit:
                            # the follower suit cannot be trumps as per the previous condition
                                wins += 1
                            elif opponent_card.suit is trumpSuit:
                            # the leader suit cannot be trumps because of the previous conditions
                                continue
                            else:
                            # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                                wins += 1
                    card_value = (wins/played)
                    hand_value += card_value

                return hand_value

            else: 
                played = 1
                for hand_card in hand_cards:

                    hand_card_points = SchnapsenTrickScorer().rank_to_points(hand_card.rank)
                    wins = 0

                    if leader_move.is_marriage():
                        opponent_card_points = SchnapsenTrickScorer().rank_to_points(leader_move.queen_card.rank)
                        if leader_move.queen_card.suit is hand_card.suit:
                        # same suit, either trump or not
                            if hand_card_points > opponent_card_points:
                                continue
                            else:
                                wins += 1
                        elif hand_card.suit is trumpSuit:
                        # the follower suit cannot be trumps as per the previous condition
                            wins += 1
                        elif leader_move.queen_card.suit is trumpSuit:
                        # the leader suit cannot be trumps because of the previous conditions
                            continue
                        else:
                        # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                            continue
                        

                    else:
                        opponent_card_points = SchnapsenTrickScorer().rank_to_points(leader_move.card.rank)

                        if hand_card.suit is leader_move.card.suit:
                            # same suit, either trump or not
                            if hand_card_points > opponent_card_points:
                                wins += 1
                            else:
                                continue
                        elif hand_card.suit is trumpSuit:
                        # the follower suit cannot be trumps as per the previous condition
                            wins += 1
                        elif leader_move.card.suit is trumpSuit:
                        # the leader suit cannot be trumps because of the previous conditions
                            continue
                        else:
                        # the follower did not follow the suit of the leader and did not play trumps, hence the leader wins
                            continue
                    
                    card_value = (wins/played)
                    hand_value += card_value

            return hand_value            
