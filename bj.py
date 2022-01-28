import random
class Shoe:
    def __init__(self,numDecks,pen):
        self.numDecks = numDecks
        self.pen = pen
        
        self.reset()

    def reset(self):
        self.numCards = 52*self.numDecks
        self.runningCount = 0
        self.trueCount = 0
        self.shoe = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4*self.numDecks
        random.shuffle(self.shoe)
    
    def pull(self):
        if self.numCards < (1-self.pen*52*self.numDecks):
            self.reset()
        
        card = self.shoe.pop()
        self.numCards -=1
        self.runningCount += self.countCard(card)
        self.trueCount = self.runningCount/(self.numCards/52)

        return card


    def countCard(self,card):
        if type(card)==str:
            return -1
        elif card < 7:
            return 1
        else:
            return 0

class Player:
    def __init__(self,bankroll):
        self.bankroll = bankroll
        self.hands= []
        self.bets = []
    
    def bet(self,trueCount,minBet):
        if trueCount <=1:
            bet = 1*minBet
        elif trueCount >= 4:
            bet = 4*minBet
        else:
            bet = trueCount*minBet
        self.bankroll -= bet
        return bet

    def play(self, hand, dealerCard,trueCount):
        move = self.basicStrategy(hand,dealerCard,trueCount)
        return move
    

    def basicStrategy(self,hand,dealerCard):
        

        hard = {
        17:['S','S','S','S','S','S','S','S','S','S'],
        16:['S','S','S','S','S','H','H','Sh','Sh','Sh'],
        15:['S','S','S','S','S','H','H','H','Sh','H'],
        14:['S','S','S','S','S','H','H','H','H','H'],
        13:['S','S','S','S','S','H','H','H','H','H'],
        12:['S','S','S','S','S','H','H','H','H','H'],
        11:['D','D','D','D','D','D','D','D','D','D'],
        10:['D','D','D','D','D','D','D','D','H','H'],
        9: ['D','D','D','D','D','H','H','H','H','H'],
        8: ['H','H','H','H','H','H','H','H','H','H'],
        }
        softs = {
        20:['S','S','S','S','S','S','S','S','S','S'],
        19:['S','S','S','S','Ds','S','S','S','S','S'],
        18:['Ds','Ds','Ds','Ds','Ds','S','S','H','H','H'],
        17:['H','D','D','D','D','H','H','H','H','H'],
        16:['H','H','D','D','D','H','H','H','H','H'],
        15:['H','H','D','D','D','H','H','H','H','H'],
        14:['H','H','H','D','D','H','H','H','H','H'],
        13:['H','H','H','D','D','H','H','H','H','H']
        }
        splits = {
        'AA':['Y','Y','Y','Y','Y','Y','Y','Y','Y','Y'],
        'TT':['N','N','N','N','N','N','N','N','N','N'],
        9:['Y','Y','Y','Y','Y','N','Y','Y','N','N'],
        8:['Y','Y','Y','Y','Y','Y','Y','Y','Y','Y'],
        7:['Y','Y','Y','Y','Y','Y','N','N','N','N'],
        6:['Y','Y','Y','Y','Y','N','N','N','N','N'],
        5:['N','N','N','N','N','N','N','N','N','N'],
        4:['N','N','N','Y','Y','N','N','N','N','N'],
        3:['Y','Y','Y','Y','Y','Y','N','N','N','N'],
        2:['Y','Y','Y','Y','Y','Y','N','N','N','N'],
        }
        value,soft,split,splitVal,blackjack = hand.handValue()
        if value > 21:
            return 'B'
        if blackjack:
            return 'BJ'
        if split:
            if splits[splitVal][dealerCard] == 'Y':
                return 'P'
            else: 
                if value > 17:
                    value = 17
                if value < 8:
                    value = 8
                return hard[value][dealerCard] 
            return splits[splitVal][dealerCard] 

        if soft: 
            return softs[value][dealerCard] 

        if value > 17:
            value = 17
        if value < 8:
            value = 8
        return hard[value][dealerCard] 

class Hand:
    def __init__(self,cards,bet=5):
        self.cards = []
        self.value = []
        self.soft = False
        self.split = False
        self.splitVal = None
        self.cards = cards
        self.bet = bet
    
    def hit(self,newCard):
        self.cards.append(newCard)
        self.value,self.soft,self.split,self.splitVal = self.handValue()
    

    def handValue(self):
        hand = self.cards
        values = {'J':10,'K':10,'Q':10,'A':11}
        splitValues = {'J':'TT','K':'TT','Q':'TT','A':'AA'}
        soft=False
        split=False
        splitVal = None
        blackjack=False
        aces = 0
        total = 0

        if hand[0]==hand[1] and len(hand)==2:
            split = True
            if type(hand[0]) == str:
                splitVal = splitValues[hand[0]]
            elif hand[0]==10:
                splitVal = 'TT'
            else:
                splitVal=hand[0]
        for card in hand:
            if type(card) == str:
                v = values[card]
                if v == 11:
                    aces+=1
                else:
                    total += v
            else:
                total += card

        if aces > 0 and total + aces-1 <= 10:
            total += 11 + aces-1
            soft=True
        else:
            total += aces

        if total == 21 and soft:
            soft=False
            blackjack = True

        return total, soft,split,splitVal,blackjack
        

sh = Shoe(8,0.8)
pl = Player(1000)
hand= Hand([sh.pull(),sh.pull()])
print(hand)
dealerCard = random.randrange(10)
print(hand.handValue(),dealerCard)
print(pl.basicStrategy(hand,dealerCard))