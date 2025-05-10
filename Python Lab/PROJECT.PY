import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in range(2, 15)
                      for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']]

    def shuffle(self):
        random.shuffle(self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def arrange_hand(self):
        self.hand.sort(key=lambda card: card.rank)

    def draw(self, deck):
        if len(deck.cards) > 0:
            self.hand.append(deck.cards.pop())
        else:
            print("Deck is empty!")

    def discard(self, card_index):
        if 0 <= card_index < len(self.hand):
            discarded_card = self.hand.pop(card_index)
            return discarded_card
        else:
            print("Invalid card index!")
            return None

class CapsaSusunGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(name) for name in players]

    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.hand = self.deck.cards[:13]
            self.deck.cards = self.deck.cards[13:]
            player.arrange_hand()
            print(f"{player.name}'s hand: {[card.rank for card in player.hand]}")

    def evaluate_hand(self, hand):
        # Placeholder for hand evaluation logic
        pass

    def play_round(self):
        for player in self.players:
            print(f"\n{player.name}'s turn:")
            action = input("Enter 'draw' to draw a card or 'discard' to discard a card: ")
            if action == 'draw':
                player.draw(self.deck)
                print(f"{player.name} drew a card.")
            elif action == 'discard':
                card_index = int(input("Enter the index of the card to discard: "))
                discarded_card = player.discard(card_index)
                if discarded_card:
                    print(f"{player.name} discarded {discarded_card.rank} of {discarded_card.suit}.")
            else:
                print("Invalid action!")

    def play_game(self):
        self.start_game()
        while True:
            self.play_round()
            # Add logic to check for game end conditions and determine the winner

# Example usage
players = ['Alice', 'Bob', 'Charlie', 'David']
game = CapsaSusunGame(players)
game.play_game()
