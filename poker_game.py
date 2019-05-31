#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:48:55 2019

@author: sandanpann
"""
import sys
import random
from collections import Counter

class Test:
    
    poker_game = Game(['Steve', 'John', 'Michael', 'Aaron'])


#%%
class Game:
    
    def __init__(self, names):
        self.deck = self.populate_deck()
        # to store a list of all the players' hands
        self.hands = {}
        # deal to every player
        for name in names:
            hand = []
            # deal 5 random cards
            for i in range(5):
                rand = random.choice(self.deck)
                hand.append(self.deck.pop(self.deck.index(rand)))
            self.hands[name] = hand
        self.get_winner(self.hands)
        print(len(self.deck))
            
    def populate_deck(self):
        deck = []
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        # fill up the deck
        for suit in suits:
            deck.append(('2', suit))
            deck.append(('3', suit))
            deck.append(('4', suit))
            deck.append(('5', suit))
            deck.append(('6', suit))
            deck.append(('7', suit))
            deck.append(('8', suit))
            deck.append(('9', suit))
            deck.append(('10', suit))
            deck.append(('J', suit))
            deck.append(('Q', suit))
            deck.append(('K', suit))
            deck.append(('A', suit))
        return deck
    
    def get_winner(self, hands):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 
                  'Q': 12, 'K': 13, 'A': 14}
        # to store the winner
        winner = ""
        # evaluating winner by high card
        high_card = 0
        # iterate through players
        for name in hands.keys():
            hand = hands[name]
            # evaluating the highest card in the hand
            hand_high_card = 0
            for card in hand:
                card_value = values[card[0]]
                if card_value > hand_high_card:
                    hand_high_card = card_value
            # evaluating whether it's the highest card
            if hand_high_card > high_card:
                high_card = hand_high_card
                winner = name
        # evaluating winner by pairs
        high_pair = 0
        for name in hands.keys():
            num_values = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
                  '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 
                  'Q': 0, 'K': 0, 'A': 0}
            hand = hands[name]
            hand_high_pair = 0
            for card in hand:
                # adding to the number of values for each card
                num_values[card[0]] = num_values[card[0]] + 1
            for value in num_values.keys():
                # checks if the value is a pair
                if num_values[value] > 1:
                    # checks whether there's previously been a pair (i.e. a pair of pairs)
                    if hand_high_pair > 1:
                        if values[value] > hand_high_pair:
                            hand_high_pair = values[value]
                        
            if hand_high_card > high_card:
                high_card = hand_high_card
                winner = name
        print(winner)
        return winner
            
#%%

def parse_arguments():
    """Here we parse the arguments that were submitted to the script"""
    arguments = sys.argv[1:]
    return arguments

def main(arguments):
    """Here is the main functionality of the script"""
    number_of_players = arguments[1]
    names = []
    for i in range(number_of_players):
        name = input("Enter Name: ")
        names.append(name)
    poker = Game(names)
        
if __name__ == '__main__':
    """This code is executed if the file is called directly from the ternminal"""
    arguments = parse_arguments()
    main(arguments)