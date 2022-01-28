from bj import *

class Table:
    def __init__(self,decks=8,pen=0.8)
        self.player = Player()
        self.shoe = Shoe(decks,pen)
        self.dealerCard = None
        
    def simulate(self):
        pass
    def dealPlayer(self,player):
        #deal two cards
        hand = Hand([self.shoe.pull(),self.shoe.pull()])
        self.player.hands.append(hand)
    
    def playHand(self,hand):
        bust = False
        move = self.player.play(hand,self.dealerCard)

        while not bust and move != 'S':
            

    