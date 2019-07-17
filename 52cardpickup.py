import random

class Card:
    value=0
    suit=0
    vName=' '
    sName= ' '
    suitNames = [None, "Hearts", "Diamonds", "Clubs", "Spades"]
    valueNames = [None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit
        
        self.sName=Card.suitNames[suit]
        self.vName=Card.valueNames[value]        
    def getCard(self):
        print(self.vName+' of '+self.sName)

class Deck:
    cardList = []
    def __init__(self):
        self.buildDeck()
        self.playPile = []
        self.discardPile = []
    
    def buildDeck(self):
        for j in range(1,13):
            for k in range (1,4):
                self.cardList.append(Card(j,k))
    
                                     
    def printDeck(self):
        for i in self.cardList:
            i.getCard()
    def shuffle(self):
        random.shuffle(self.cardList)

    def drawCard(self, Deck):
        return self.cardList.pop(0)

class Player(Deck):                 
     playerName = ''
     def __init__(self,name):
         self.buildDeck()
         self.playerName=name

     def buildDeck(self):
        for j in range(1,13):
            for k in range (1,4):
                self.cardList.append(Card(j,k))
    
                                     
     def printDeck(self):
        for i in self.cardList:
            i.getCard()
     def shuffle(self):
        random.shuffle(self.cardList)


player1 = Player('Misha')
player1.printDeck()
##
deck1=Deck()
deck1.printDeck()
print('--------------------------------------------')
deck1.shuffle()
deck1.printDeck()
##print('--------------------------------------------')
##deck1.shuffle()
##deck1.printDeck()
##print('--------------------------------------------')
##deck1.shuffle()
##deck1.printDeck()
##            
