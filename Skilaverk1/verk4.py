#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
class Card():
    def __init__(self, suit, value, isHidden):
        self.suit = suit #strengur
        self.value = value #strengur
        self.hidden = isHidden #boolean

        if(value == 'A'): #A er as
            self.pointValue = 11
        elif value in ['K', 'Q', 'J']: #kóngur, drottning, gosi
            self.pointValue = 10
        elif value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']: #Spil frá 2 uppí 10
            self.pointValue = int(value) #int(value) convertar tölunni í int

    def __str__(self):
        #Þetta function mun segja til um hvað lit spilið hefur á forminu [SV] (suit og value) eða [XX} ef spilið er falið
        if(self.hidden):
            return '[XX]'
        else:
            return '[' + str(self.value) + self.suit + ']'

    def getSuit(self): #Sækir suit eða [SX] spilsins
        return self.suit

    def getValue(self): #Sækir value eða [XV] spilsins
        return self.value

    def setPointValue(self, pointValue): #Setur pointValue [1-10, J, Q, K, A] spilsins
        self.pointValue = pointValue

    def isHidden(self):
        return self.hidden

    def hideCard(self): #Gefur spilinu [SV] = [XX] sem þýðir að það sé falið
        self.hidden = True

    def revealCard(self): #Sýnir [SV] value spilsins
        self.hidden = False

    def isAce(self): #Ef spilið er ás þá setur það value'ið spilsins á [XA]
        return self.value == 'A'

class Deck():
    #52 objecta listi sem samsvarar spilastokki, hægt er að breyta/eyða hlutum úr listanum
    def __init__(self):
        cardsInDeck = [] #Tómur listi fyrir spil
        suits = ['S', 'H', 'D', 'C'] #Litir(suits) á spilum [SX]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #Values fyris spil [XV]

        for s in suits:
            for v in values:
                cardsInDeck.append(Card(s,v,False))
        self.cardsInDeck = cardsInDeck[:]

    def __str__(self): #sýnir fjölda spila eftir í stokknum
        return 'The deck has ' + str(len(self.cardsInDeck)) + ' cards left.'

    def dealCard(self): #Deal'ar spilum
        card = random.choice(self.cardsInDeck)
        self.cardsInDeck.remove(card)
        return card

class Hand():
    #Hönd spilara
    def __init__(self, bet=1):
        self.cards = []
        self.values = []
        self.validMoves = []
        self.bet = bet

    def addCard(self, card):
        self.cards.append(card)
        self.updateValues()
        self.updateValidMoves()

    def updateValidMoves(self):
        moves = ['Stay'] #Ef að spilari er með 21
        for value in self.values:
            if value > 21:
                self.validMoves = 'Bust'
                return
            if value == 21:
                if len(self.cards) == 2:
                    self.validMoves = 'Blackjack'
                    return
                self.validMoves == '21'
                return
        moves.append('Hit')

        if len(self.cards) <= 2:
            moves.append('Double')
        if len(self.cards == 2):
            if self.cards[0].value == self.cards[1].value:
                moves.append('Split')
        self.validMoves = moves

    def updateValues(self): #Reikna value af hendinni
        v = [0]
        hasAce = False

        

