# http://www.codeskulptor.org/#user38_FQYT1KOJzW_16.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        
    def __str__(self):
        out = ""
        for hand in self.hand:
            out += hand.__str__() + " "
        return "Hand contains " + out 

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        ace = 0
        for i in self.hand:
            if i.get_rank() == 'A':
                ace += 1
            hand_value += VALUES[i.get_rank()]
        if (ace > 0) and (hand_value + 10) <= 21:
            hand_value += 10
        return hand_value
    
    def draw(self, canvas, pos):
        for i in self.hand:
            i.draw(canvas, pos)
            pos[0] += 82
                
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(str(suit), str(rank)))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        out = ""
        for i in range(len(self.deck)):
            out += str(self.deck[i]) + " "
        return "Deck contains " + out

deck = Deck()
p_hand = Hand()
d_hand = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, p_hand, d_hand, deck, score
    deck = Deck()
    p_hand = Hand()
    d_hand = Hand()
    if in_play:
        score -= 1
    deck.shuffle()
    for i in range(2):
        p_hand.add_card(deck.deal_card())
        d_hand.add_card(deck.deal_card())
    in_play = True
    outcome = "Hit or stand?"

def hit():
    global p_hand, in_play, score, outcome
    p_hand.add_card(deck.deal_card())
    if (p_hand.get_value() > 21):
        in_play = False
        score -= 1
        outcome = "You have busted, new deal?"

def stand():
    global d_hand, in_play, score, outcome
    in_play = False
    while (d_hand.get_value() < 17):
        d_hand.add_card(deck.deal_card())
    if (d_hand.get_value() > 21):
        score += 1
        outcome = "Dealer has busted, you win!"
    elif (d_hand.get_value() >= p_hand.get_value()):
        score -= 1
        outcome = "Dealer wins! New deal?"
    else:
        score += 1
        outcome = "Player wins! New deal?"

# draw handler    
def draw(canvas):
    canvas.draw_text("Score: " + str(score), [400, 100], 35, "Black")
    canvas.draw_text("Black Jack", [50, 100], 55, "Aqua")
    canvas.draw_text("Dealer", [50, 200], 40, "Black")
    canvas.draw_text("Player", [50, 400], 40, "Black")
    canvas.draw_text(outcome, [200, 200], 30, "Black")
    p_hand.draw(canvas, [70, 440])
    d_hand.draw(canvas, [70, 240])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [70 + CARD_BACK_CENTER[0], 240 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
