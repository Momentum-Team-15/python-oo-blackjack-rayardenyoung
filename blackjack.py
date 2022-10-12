# Write your blackjack game here.

#1. Outline/list out my classes
#2. Flesh out classes(first just of card) with attributes def __init__ & __str__
#3. Build one card
#4. Don't want to build all cards by hand, so build constants [list] of suits
#5. Build dictionary of key value pairs: 'K: 10', etc
#6. Build a whole deck
    #start with empty deck variable, build loop
    #move function into deck class. change deck variable to be a object, with one attribute being the cards
#7. make a new deck

import random
# Outline my classes
SUITS = ['♥️', '♣️', '♦️','♠️']
RANK_VALUES = {
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': 11,
    #TODO handle when ace is 1 when calculating points
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9, 
    10: 10,
}


class Game:
    
    def __init__(self):
        self.deck = Deck('Bicycle')
        # make a new deck of cards, which calls __init__() method
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        self.deal_card(self.dealer)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.player)

        print("The dealer's cards are: ")
        for card in self.dealer.hand:
            print(card)
            #call method you created in calculate_hand > pass self.dealer as argument in calculate_hand
        print(f'This hand is worth {self.calculate_hand(self.dealer)}\n')

        print("The player's cards are: ")
        for card in self.player.hand:
            print(card)
            #call method you created in calculate_hand > pass self.player as argument in calculate_hand
        print(f'This hand is worth {self.calculate_hand(self.player)}')

        print(f'There are now {len(self.deck.cards)} cards in the deck\n')


    def deal_card(self, participant):
        #what do you want to happen when you deal?
        #take one card from the deck and put it in player/dealer's hand
        #what parameters does it need? a participant (player or dealer)
        #take a card
        card = self.deck.cards.pop()
        #add card to participant's hand
        participant.hand.append(card)
    
    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        #return value of hand instead of storing it in variable, because value changes
        return total_points
        
        

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    def __str__(self):
        return f'{self.rank} of {self.suit}'
# *****************************************************
# example of building one card
# queen_of_hearts = Card('♥️', 'Q', 10)
# print(f'{queen_of_hearts} is worth {queen_of_hearts.value}')
# build a whole deck
# *****************************************************
class Deck:
    def __init__(self, brand):
        self.cards = []
        self.brand = brand
        self.used = False
        for suit in SUITS:
            for rank_value in RANK_VALUES.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)
    def __str__(self):
        return f'{self.brand} deck of {len(self.cards)} cards'
    def shuffle(self):
        random.shuffle(self.cards)

#in class with Webster >>>>
#can't call Deck(just a blueprint), instead make it into an instance (variable)
# my_deck = Deck('Bicycle')
# #calling the method .shuffle on the instance (variable) of my_deck
# my_deck.shuffle() #>> could add this to line 68 as self.shuffle() to make this part of __init__ method
# for card in my_deck.cards:
#     print(card)


class Player:
    def __init__(self):
        self.hand = []
class Dealer:
    def __init__(self):
        self.hand = []

#new_game = Game()
#Game is a class that holds all the other classes, and initiates the game
#print the shuffled cards>>
# for card in new_game.deck.cards:
#     print(card)

#deal a card to this new_game's dealer (x2)>>
# new_game.deal_card(new_game.dealer)
# new_game.deal_card(new_game.dealer)
# # print(new_game.dealer.hand)
# #^^^^prints object, good first step
# print("The dealer's cards are: ")
# for card in new_game.dealer.hand:
#     print(card)

# #copy but for player>>
# new_game.deal_card(new_game.player)
# new_game.deal_card(new_game.player)

# print("The player's cards are: ")
# for card in new_game.player.hand:
#     print(card)

# #run a print statement to check that it's taking cards out of the deck>>
# print(f'There are now{len(new_game.deck.cards)} cards in the deck')

#once you've finished...move all this^^^ to the Game class and switch out instance of 'new_game' for 'self'

#game play conditionals>>
# instantiates the game, calls the __init__() method
# check if dealer has 21
def play_game():
    # TODO make player go first
    if new_game.calculate_hand(new_game.dealer) == 21:
        # dealer has blackjack
        print('Dealer has blackjack!')
        if new_game.calculate_hand(new_game.player) == 21:
            # player also has blackjack
            print('Push')
            return
        else:
            print(f'Player loses with {new_game.calculate_hand(new_game.player)}')
            # player does not also have blackjack
            return  
    elif new_game.calculate_hand(new_game.player) == 21:
        # dealer does not have blackjack but player does
        print('Player wins with blackjack!')
        return
    # nobody has blackjack, only get here if we don't hit any of the 
    # above return statements. This is the dealer's turn
    while new_game.calculate_hand(new_game.dealer) < 17:
        new_game.deal_card(new_game.dealer)
        print('Dealer hits')
        if new_game.calculate_hand(new_game.dealer) > 21:
            print(f'Dealer busted with {new_game.calculate_hand(new_game.dealer)}!')
            break

        elif new_game.calculate_hand(new_game.dealer) == 21:
            print('Dealer wins with 21!')
            break
# we reach here only if the dealer has at least 17 but less than 21
    else:
        print(f"Dealer's hand is: ")
        [print(card) for card in new_game.dealer.hand]
        # this list comprehension is shorthand for
        # for card in new_game.dealer.hand:
            # print(card)
        print(f"Player's hand is: ")
        [print(card) for card in new_game.player.hand]
        # player now chooses whether to hit or stay    
#>>>>this is where the game should start if player goes first
        choice = ''
        while choice != 's':
            choice = input("Would you like to (h)it or (s)tay ").lower()
            if choice == 'h':
                new_game.deal_card(new_game.player)
                print(f"Player's hand is: ")
                [print(card) for card in new_game.player.hand]
                if new_game.calculate_hand(new_game.player) == 21:
                    print("Player wins with 21!")
                    break
                elif new_game.calculate_hand(new_game.player) > 21:
                    print("Player busts!")
                    break
            elif choice == 's':
                print("Player stays")
                print(f"Player's hand is: ")
                [print(card) for card in new_game.player.hand]
            else:
                print("Please choose 'h' or 's'")
        else: 
            print(f"Dealer's hand is: ")
            [print(card) for card in new_game.dealer.hand]
            print(f"Player's hand is: ")
            [print(card) for card in new_game.player.hand]
            # determine if player has more points than dealer
            dealer_points = new_game.calculate_hand(new_game.dealer)
            player_points = new_game.calculate_hand(new_game.player)
            if dealer_points > player_points:
                print(f'Dealer wins with {dealer_points}. Player has {player_points}')
            elif player_points > dealer_points:
                print(f'Player wins with {player_points}. Dealer has {dealer_points}')
            else:
                print(f"It's a draw. Both have {dealer_points}")
new_game = Game()
play_game()