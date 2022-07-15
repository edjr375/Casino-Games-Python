
import random
import os

class Player:

    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

class Deck_of_Cards:
    #This class creates a deck of card list and a dictionay of each cards value
    def __init__(self):
        self.deck = Deck_of_Cards.create_deck(self)
        self.card_value = Deck_of_Cards.card_value(self.deck)

    #creates a deck of cards
    def create_deck(self):
        deck = []
        for suit in suits:
            for card in cards: 
                deck.append(card + ' of ' + suit)
        return deck   
    #adds a value to each card in a dictionay key = card, value = card value
    def card_value(deck):
        card_values = {}
        for i in range (0,13):
            if 'Ace' in deck[i]:
                card_values[deck[i]] = 11
            elif i > 9:
                card_values[deck[i]] = 10
            else:
                card_values[deck[i]] = i + 1
        for i in range (13,26):
            if 'Ace' in deck[i]:
                card_values[deck[i]] = 11
            elif i > 22:
                card_values[deck[i]] = 10
            else:
                card_values[deck[i]] = i - 12 
        for i in range (26,39):
            if 'Ace' in deck[i]:
                card_values[deck[i]] = 11
            elif i > 34:
                card_values[deck[i]] = 10
            else:
                card_values[deck[i]] = i - 25 
        for i in range (39,52):
            if 'Ace' in deck[i]:
                card_values[deck[i]] = 11
            elif i > 48:
                card_values[deck[i]] = 10
            else:
                card_values[deck[i]] = i - 38 
        return card_values
    
    def print_deck (self):
        print(self.deck)

def clear():
    os.system('clear')

def deal(deck):
    card_value = 0
    cards = []
    while len(cards) < 2:
        card = random.choice(deck.deck)
        cards.append(card)
        card_value += deck.card_value[card]
        deck.deck.remove(card)
    return cards, card_value

def blackjack(deck, player_score, dealer_score):
    #deal 2 cards to the player and the dealer and calcualte the card vaules
    player_cards, player_value = deal(deck)
    dealer_cards, dealer_value = deal(deck)
    #print Players hand
    print("Players Cards:")
    for i in range(2):
        print(player_cards[i])
    print('\n')
    #print first card in dealers hand
    print("Dealers Cards: ")
    print(dealer_cards[0])
    print('\n')
    
    # loop continues until players card values are greater than 21
    while player_value <= 21:
        #CHecks players original card values equal 21 "Blackjack" or over 21 "Bust"
        if player_value == 21:
            print('Blackjack!')
            print('You Win!')
            player_value = 22
            player_score += 1
            break
        
        #Player is given the choice to hit or stand
        choice = input('Type H for Hit or S for Stand: ')
        if choice.upper() != 'H' and choice.upper() != 'S':
            print('Invalid Response')
            print(' H for Hit or S for Stand')
        
        #if player hits, new card is drawn and added to players card value
        if choice.upper() == 'H':
            player_card = random.choice(deck.deck)
            player_cards.append(player_card)
            player_value += deck.card_value[player_card]
            deck.deck.remove(player_card)
            print(player_cards,' ', player_value)
        
        if player_value > 21:
            print('Bust!')
            print('You Lose')
            dealer_score += 1
            break
        
        #if player stand, checks dealer card vaule for 21 (dealer gets blackjack, player loses)
        if choice.upper() == 'S':
            print(dealer_cards)
            if dealer_value == 21:
                print('Dealer had Blackjack, You Lose!')
                player_value = 22
                dealer_score += 1
                break
            while dealer_value <= 21:
                if dealer_value < 17: 
                    print('Dealer Hits')
                    dealer_card = random.choice(deck.deck)
                    dealer_cards.append(dealer_card)
                    dealer_value += deck.card_value[dealer_card]
                    deck.deck.remove(dealer_card)
                    print(dealer_cards)
                if dealer_value > 21:
                    print('Dealer Busts!')
                    print('You Win!')
                    player_value = 22
                    player_score += 1
                    break
                if dealer_value >= 17:
                    if player_value > dealer_value:
                        print('Player Hand: ', player_cards, player_value)
                        print('Dealers Hand: ', dealer_cards, dealer_value)
                        print('You Win!')
                        player_value = 22
                        player_score += 1
                        break
                    if player_value < dealer_value:
                        print('Player Hand: ', player_cards, player_value)
                        print('Dealers Hand: ', dealer_cards, dealer_value)
                        print('You Lose!')
                        player_value = 22
                        dealer_score += 1
                        break
                    if player_value == dealer_value:
                        print('Player Hand: ', player_cards, player_value)
                        print('Dealers Hand: ', dealer_cards, dealer_value)
                        print('Tie')
                        player_value = 22
                        break
    again = ' '
    while again.upper() != 'Y' and again.upper() != 'N': 
        print('Players Score: {}'.format(player_score))
        print('dealers score: {}'.format(dealer_score))
        again = input('Would you like to Play again? (Y or N): ' )
        if again.upper() != 'Y' and again.upper() != 'N':
            print('Invalad answer. Y or N: ' )
        if again.upper() == 'Y':
            clear()
            deck = Deck_of_Cards()
            blackjack(deck, player_score, dealer_score)

            
    
clear()
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

print ('BlackJack Terminal Game!')

player_score = 0
dealer_score = 0
deck = Deck_of_Cards()

blackjack(deck, player_score, dealer_score)
#print('Players Score: {}'.format(player_score))
#print('dealers score: {}'.format(dealer_score))
print('Thanks for Playing')



