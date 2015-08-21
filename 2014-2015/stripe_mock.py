import random

class Deck:
  def __init__(self, withJokers = False):
    self.cards = []
    for i in range(1, 14):
      for j in range(4):
        self.cards.append(i)

  def takeCard(self):
    if (len(self.cards) == 0):
      return None
    randomCardIndex = random.randint(0, len(self.cards))
    returnVal = self.cards[randomCardIndex]
    self.cards.remove(returnVal)
    return returnVal

  def takeAce(self):
    self.cards.remove(1)
    return 1

class Player:
  def __init__(self, deck):
    self.threshold = 21
    #current val of cards in hand
    self.count = 0
    self.done = False
    self.deck = deck
    self.hasAce = False

  #return bustVal if the player busts 0 otherwise
  def hit(self, drawAce = False):
    card = self.deck.takeAce() if drawAce else self.deck.takeCard() 
    self.count += card
    #if the card is an ace
    if (card == 1):
      print "DREW ACE!"
      self.hasAce = True
      if (self.count + 12 <= self.threshold):
        self.count += 12
    #if player busts
    if (self.count > self.threshold):
      if (self.hasAce):
        self.count -= 12
      self.done = True
      #score is 0 because he busted
      bustVal = self.count
      self.count
      return bustVal
    return card

  def stay(self):
    self.done = True
    if self.hasAce:
      self.count += 12

def allPlayersDone(players):
  for p in players:
    if not p.done:
      return False
  return True

def playGame():
  numPlayers = int(input("How many players are playing?"))
  deck = Deck()
  players = [Player(deck) for i in range(numPlayers)]
  #while not all players are done...
  while (not allPlayersDone(players)):
    for i in range(numPlayers):
      #if the player has finished, skip over the player
      if (players[i].done):
        continue
      print "----------------------------"
      print "You are player #", (i+1)
      print "Current count = ", players[i].count
      hit = int(input("do you want to hit? (1 = yes, 0 = no)"))
      #hit case
      if (hit >= 1):
        hitVal = 0
        if hit>1:
          hitVal = players[i].hit(True)
        else:
          hitVal = players[i].hit()
        
        #if bust
        if (hitVal > 21): 
          print "you busted at ", hitVal
        else:
          print "You drew the card ", hitVal
          print "Your count is now =", players[i].count
      #stay case
      else:
        print "You stayed at ",players[i].count


playGame()


