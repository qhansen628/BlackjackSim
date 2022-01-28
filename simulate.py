import * from bj

class Table:
    def __init__(self,decks=8,pen=0.8)
        self.players = Player()
        self.shoe = Shoe(decks,pen)
        self.dealerCard = None
        
    def simulate(self):
        pass
    def dealPlayer(self,player):
        
        for hand in player.hands:
            self.playHand(hand,)
    
    def playHand(self,hand,player):
        bust = False
        move = player.play(hand,self.dealerCard)

        while not bust and move != 'S':
            

    