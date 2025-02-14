import random

class Cards():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.value}{self.suit}" #Print from return
    def __repr__(self):
        return f"{self.value}{self.suit}" #Print from print command

class Decks():
    def __init__(self):
        suits = ['\u2665','\u2663','\u2666','\u2660']
        values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

        self.deck = []
        self.card_pile = []
        for suit in suits:
            for value in values:
                self.deck.append(Cards(suit,value))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        self.hands = []
        for i in range(2):
            self.hands.append([]) #Creates sublist for two players
        
        #To Do: Insert alternating values 7 times
        for i in range(len(self.hands)):
            self.hands[i].extend(self.deck[:7])
            del self.deck[:7]
            print(f"Player {i+1} Hand - {self.hands[i]}")
        
        # ***IMPORTANT - Returns the self.hands list to access in
        # class Play() ***
        if self.deck:
            self.card_pile.append(self.deck.pop(0))
        return self.hands 

class Play():
    def __init__(self,hands,deck,card_pile):
        self.hands = hands
        self.deck = deck
        self.card_pile = card_pile

    def reset(self):
            print(f"\nCurrent Card: {self.card_pile[-1]}\n")

    def remove_unicode(self,text):
        return text.encode("ascii","ignore").decode()

    def game(self):
        #To Do: Player 1 can play either:
        turn = 0
        stack = 2
        self.cards_playable = []
        while True:
            if not self.hands[turn]:
                print(f"Player {turn+1} Wins!")
                return

            self.reset()
            for card in self.hands[turn]:
                if card.value == 'A': value = 14
                elif card.value == 'K': value = 13
                elif card.value == 'Q': value = 12
                elif card.value == 'J': value = 11
                else: value = int(card.value)

                top_card = self.card_pile[-1]
                if top_card.value == 'A': top_value = 14
                elif top_card.value == 'K': top_value = 13
                elif top_card.value == 'Q': top_value = 12
                elif top_card.value == 'J': top_value = 11
                else: top_value = int(top_card.value)

                if (value == top_value) or (card.suit == top_card.suit) or (value==8):
                    self.cards_playable.append(card)
            
            if not self.cards_playable:
                self.hands[turn].append(self.deck[0])
                print(f"Player {turn+1} Drew a card... {self.deck[0]}\n")
                self.deck.pop(0)
            else:
                if (len(self.cards_playable))>= 2:
                    choice_options = f"{self.cards_playable} (ex. 1-{len(self.cards_playable)})"
                else:
                    choice_options = f"{self.cards_playable} (ex. 1)"
                while True:
                    try:
                        choice = int(input(f"Player {turn+1} | Pick Choice - {choice_options}: "))-1         
                        if 0<=choice<(len(self.cards_playable)):
                            break
                        print(f"\nInvalid Choice | Please enter a number between 1 and {len(self.cards_playable)}.") #Types in a number beyond the numer restriction
                    except ValueError:
                        print("\nInvalid Input! | Please enter a positive integer.") #Types in a letter
                selected_card = self.cards_playable[choice]
                self.hands[turn].remove(selected_card)
                if self.remove_unicode(str(selected_card)) == '8':
                    while True:
                        new_suit = (input(f"\nPlayer {turn +1} | Enter new suit (hearts, diamonds, spades, clubs): ").lower())
                        suit_map = {'hearts':'\u2665','clubs':'\u2663','diamonds':'\u2666','spades':'\u2660'}
                        if new_suit in suit_map:
                                selected_card = Cards(suit_map[new_suit], 8)
                                print(f"Player {turn+1} has changed the suit to {suit_map[new_suit]}\n")
                                break
                        else:
                            print("\nInvalid Input! | Please enter a valid suit.")
                self.card_pile.append(selected_card)
                self.cards_playable=[]

            if self.remove_unicode(str(self.card_pile[-1])) == '2':
                if self.remove_unicode(str(self.card_pile[-2])) == '2':
                    stack += 2
                else:
                    stack = 2
                if turn == 0:
                    self.hands[1].extend(self.deck[0:stack])
                else:
                    self.hands[0].extend(self.deck[0:stack])
                del self.deck[0:stack]

            if self.remove_unicode(str(self.card_pile[-1])) == 'A':
                continue
            elif turn == 1:
                turn = 0
            else: 
                turn = 1

            for i in range(len(self.hands)):
                print(f"Player {i+1} | {self.hands[i]}")

deck = Decks()

hands = deck.deal()
if hands:
    play = Play(hands,deck.deck,deck.card_pile)
    play.game()
