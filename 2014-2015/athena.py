from random import shuffle
import math

class Deck:
  def __init__(self):
    self.deck = []
    for i in range(1, 14):
      for j in range(4):
        self.deck.append(i)

  def shuffle(self):
    shuffle(self.deck)

  def takeCard(self):
    return_val = self.deck.pop(0)
    return return_val

def policy():
  policy = {}
  for i in range(1, 14):
    scaled_val = float(i)/13*10 - 1
    down = int(math.trunc(scaled_val))
    up = int(math.ceil(scaled_val))
    if (i==1):
      policy[i] = [0]
    elif (i==13):
      policy[i] = [9]
    elif (round(scaled_val) == up):
      policy[i] = [up, down]
    else:
      policy[i] = [down, up]
  return policy


class Game:
  def __init__(self, deck, policy):
    self.accept_cards = [None]*10
    self.discard_pile = []
    self.deck = deck
    self.policy = policy

  def isWon(self):
    if None in self.accept_cards:
      return False
    return True

  def isLost(self):
    return len(self.discard_pile)>=6

  def playMove(self):
    card = self.deck.takeCard()
    moves = self.policy[card]
    accepted = False
    for move in moves:
      # import pdb; pdb.set_trace()
      if (not accepted and (self.accept_cards[move] == None or self.accept_cards[move]==card)):
        #accepted the card, and put it in the slot move
        self.accept_cards[move] = card
        accepted = True
    if not accepted:
      self.discard_pile.append(card)

  def showState(self):
    print "slots ", self.accept_cards
    print "discard ", self.discard_pile

iterations = 10000
wins = 0
losses = 0
for i in range(iterations):
  deck = Deck()
  deck.shuffle()
  g = Game(deck, policy())
  while(not(g.isWon() or g.isLost())):
    g.playMove()

  
  if (g.isWon()):
    wins+=1
  else:
    losses+=1
print "winning % =",float(wins)/iterations



