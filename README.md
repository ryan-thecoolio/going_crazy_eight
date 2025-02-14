# going_crazy_eight
i went crazy coding, debugging, and playing this... (its crazy eight but scuffed)

Follow up to my war card game began coding at night 2/13/2025 finished at 3:30 pm next day; Used some AI. I did not know how to split the integer strings and the unicode and also to map suits when a user creates a new suit from playing eighth card.

Other than the initial war game, this was the first time I used classes to hold functions. After briefly reviewing, it is obvious I am still using classes and functions wrong. Half the code is inside one function 💀

# Intuition:
More like outline but, create three classes:
1. Cards - Holds the individual suits and face value of the cards such as 4♠
2. Deck - Create a standard 52 deck
3. Play - Ability for two players to interact and choose their card

# Approach

For all classes, the initial function need to be initialized:

```
def __init__(self):
	<code>
```

The parameter may include more than one in other classes to retrieve and use objects I created in previous classes such as accessing the deck.

==**Class Cards**==
Of course I need to store the values and suits, so In the first class: the parameters include value and suit:

```
def __init__(self,suit,value):
	self.suit = suit
	self.value = value
```

There is two other functions to enable users to see what is print:
```
def __str__(self):
	return f"{self.value}{self.suit}" #Print from return
def __repr__(self):
	return f"{self.value}{self.suit}" #Print from print command
```

==**Class Deck**==
Now, I assign each value in a standard 52 French 🥖 card deck 🃏 its unique attributes. This is done through a double for loop, one to iterate through the four types of suits and inside, the 13 distinct values 2 through K. All of these values I append into a list, self.cards, in order for me to later use this in the class Game.

```
class Decks():
    def __init__(self):
        suits = ['\u2665','\u2663','\u2666','\u2660']
        values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

        self.deck = []
        self.card_pile = []
        for suit in suits:
            for value in values:
                self.deck.append(Cards(suit,value))
```

Then there are two vital things to do:
4. Shuffle the Deck
5. Deal 7 cards to two players

For this first part, I simply import the random function and use the built-in function random.shuffle(a) to randomize 52! (8.0658e+67) possibilities! Thankfully, I do not have to manually do that.

```
class Decks():
	def shuffle(self):
		random.shuffle(self.cards)
```

Next, to deal 7 cards we have to:
* Call shuffle function
* Create a new list to contain both player 1 and player 2 hands
* Create a sub list in this new list through a for loop
	* While I could simply just off the bat add two lists, it is more scalable, especially since my code is turn-based and can be easily altered to accommodate more players
* Distribute seven cards to the two players
* Remove the total of 14 cards taken from self.deck()

```
class Decks():
	def deal(self):
		self.shuffle()
		self.hands = []
		for i in range(2):
			self.hands.append([])
		
		for i in range(len(self.hands)):
			self.hands[i].extend(self.deck[:7])
			del self.deck[:7]
			print(f"Player {i+1} Hand - {self.hands[i]}")
```

Finally create the first card to start
* Create a list and add the first card from self.deck()
* Remove index 0 from self.deck()

```
class Decks():
	def deal(self):
		...
		if self.deck:
			self.card_pile.append(self.deck.pop(0))
		return self.hands 
```

==**Class Play**==
First, we need to be able to access the deck and hands we created for our two players:
```
class Play():
    def __init__(self,hands,deck,card_pile):
        self.hands = hands
        self.deck = deck
        self.card_pile = card_pile
```

So, every time a card is added to the end of the list or the top of the stack, I did not actually clear the list containing the pile of card, i.e., self.card_pile, instead I simply just indexed the last element of the list. This also let me access the previous element had I not kept all elements in the list.

The function simply prints out the current top card. Now that I think about there is no point in this function...

```
class Play():
	def reset(self):
			print(f"\nCurrent Card: {self.card_pile[-1]}\n")
```

The second helper function is meant to separate the ascii characters which is the value in the cards Class such as 1,2,3,4,5,...,J,Q,K from the unicode characters or the suits. I use this when the user has an eight, two, or ace because after checking that the two or ace is a playable card (eight ignores if the hand has the same suit or value; I will explain more about this later).

In the function, I encode and the ascii characters and ignore the second half and the decode converts the encoded long byte item back to a string type that is readable. It takes in the parameter text, so that I can apply it to any string.

```
class Play()
	def remove_unicode(self,text):
		return text.encode("ascii","ignore").decode()
```


==**def game(self)**==
Now the main function, first I outline the local variables accessible throughout the numerous loops

1. The turns represent the player turn, if it is 0, then player 1 goes, otherwise player 2 goes.
2. Stack refers to the ability for users to stack twos forcing the opposing player to collect cards based on stack, which starts at 2.
3. To make it easier for the player, I automatically provide users the cards they can play.

```
class Play()
	def game(self):
		turn = 0
		stack = 2
		self.cards_playable = []
```

Next, I create a while loop until there is a winner which contains majority of the interactive gameplay. The code checks if either player hands are empty by check if either self.hands[0] or self.hands[1] is empty and based on the value, it prints either player 1 or player 2 has won and then returns the function.

```
class Play()
	def game(self):
		...
		while True:
			if not self.hands[turn]:
				print(f"Player {turn+1} Wins!")
				return
```

Otherwise, this if statement is ignored. At the beginning I call the self.reset() function I created earlier which simply prints the current top card.

Next, I create numerous if statements to assign card values from the Card(value,suit) which descend from 14 to 11 (A-J), although these numeric values hold no actual importance in terms of its 'value.' Instead I use this to compare the integers of the top card.

```
class Play():
	def game(self):
		...
		while True:
			...
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
```

* Now that I reflect, I realize I could have just compared off the bat using its string values. While it might be a less messy code, currently my only thoughts on how to implement it would be:

```
class Play():
	def game(self):
		...
		while True:
			...
			for i in range (len(self.hands[turn])):
				if self.card_pile[-1] == self.hands[turn][i]:
					self.card_playable.append(self.hands[turn][i])
```

* However, the way I wrote my code is messy, and using this method would cause more problems, since my variables are rarely named...

Afterwards, there are two possibilities:
1. The player does not have any cards they can play - self.card_playable list is empty
2. The player has at least one card to play

For the first option, the player is forced to draw a card, which removes a card from the deck. It is pretty much the same way I implement the draw seven cards each at the start of the game

```
class Play():
	def game(self):
		...
		while True:
			...
			if not self.cards_playable:
				self.hands[turn].append(self.deck[0])
				print(f"Player {turn+1} Drew a card... {self.deck[0]}\n")
				self.deck.pop(0)
```

Now, if the user has a card, then we provide the user the option to pick the card based on its index. Since the input choice range is a minimum of 1 but no greater than the length of self.card_playable, I use a while loop and a try and except to ensure the value the user inputs is NOT an illegal choice or a string. 

I also print an asthetically pleasing to understand input by providing the user which value they should input through choice_options. Also, since the minimum is 1, I have to subtract 1, since an index starts at 0.

```
class Play():
	def game(self):
		...
	while True:
		...
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
					print(f"\nInvalid Choice | Please enter a number between 1 and {len(self.cards_playable)}.")
				except ValueError:
					print("\nInvalid Input! | Please enter a positive integer.")
```

Whichever, choice they pick, I use it as an index to get the actual value in a variable called ``selected_card``. As a result, I also remove the ``select_card`` from the players hand

```
class Play():
	def game(self):
		...
	while True:
		...
		selected_card = self.cards_playable[choice]
		self.hands[turn].remove(selected_card)
```

Now, there are another two possibilities:
1. The number is eight - Has a unique property to change the current suit
2. The number is not eight - Number does not change suit

In the first case, I use the earlier ``def remove_unicode(self,text) or self.remove_unicode`` to read if the value is eight. If it is eight, then I provide the player the option to input any of the four suits. To ensure that the user types a valid suit, I created a dictionary and if the input is in this dictionary, then it is accepted as a playable card. The card becomes ``Card(suit_picked, 8)`` 

```
class Play():
	def game(self):
		...
	while True:
		...
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
```

If it is a regular non-eight card, then it dismisses this if statement and similar to an eight-card, it becomes appended onto the ``self.card_pile``. At the same time, I empty the ``self.cards_playable`` to avoid allowing the next turn to have the option of the other player's card.

```
class Play():
	def game(self):
		...
		while True:
			...
	        self.card_pile.append(selected_card)
	        self.cards_playable=[]		
```

While, the top card has now been decided, there are two additional abilities that a card holds.

If the top card is a 2 or an ace.

1. If it is a two, the player is forced to pick up at least 2 cards. But if it is stacked, by using the stack variable which is compounded based on the number of times 2 has been played consecutively. 
2. An ace will forcibly cause the next player to lose their turn, in other words, give the current player another turn.

```
class Play():
	def game(self):
		while True:
			...
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
```

That's basically it, and to call and start the game:

```
deck = Decks()

hands = deck.deal()
if hands:
    play = Play(hands,deck.deck,deck.card_pile)
    play.game()
```


# Improvements
1. I gave up on trying to decide who gets to go first. ~~While I know I can randomize through ``random.randint(0,1)``~~ Nevermind, now that I have created a turns variable, I can simply just set the first turn.
2. Implement the ability for more players
3. Make it actually user-friendly --> HTML, CSS and JS :(
4. Code less messy as well as unnecessary code
