import random
from sys import argv

scripts, x, y = argv

amountCards = 52

class kort:
    def __init__(self, colour, number, value):
        self.colour = colour
        self.number = number
        self.blackjack_value = value

class player:
    def __init__(self, player_number, cards):
        self.player_number = player_number
        self.cards = cards
        self.sum = 0
    def sum_blackjack(self):
        all_kort = []
        for i in self.cards:
            all_kort.append(i.blackjack_value)
        sum_b = sum(all_kort)
        return sum_b
    
    
def genCards(amount):
    list = []
    i = 1
    x = 1
    y = 1
    
    while x <= (amount / 52):
    
        while i <= 13:
            if y > 10:
                list.append(kort("Hearts", i, 10))
                i += 1
            else:
                list.append(kort("Hearts", i, i))
                i += 1
                y += 1
        
        y = 1
        i = 1
        
        while i <= 13:
            if y > 10:    
                list.append(kort("Spades", i, 10))
                i += 1
            else:
                list.append(kort("Spades", i, i))
                i += 1
                y += 1
        
        y = 1
        i = 1
        
        while i <= 13:
            if y > 10:
                list.append(kort("Diamonds", i, 10))
                i += 1
            else:
                list.append(kort("Diamonds", i, i))
                i += 1
                y += 1
        
        y = 1
        i = 1
        
        while i <= 13:
            if y > 10:
                list.append(kort("Clubs", i, 10))
                i += 1
            else:
                list.append(kort("Clubs", i, i))
                i += 1
                y += 1
        
            
        i = 1
        x += 1
        
    return list

def printDeck(deck, amount):
    for i in range(0, amount):
        print(deck[i].colour, deck[i].number, deck[i].blackjack_value)
        
def shuffle(list, times): 
    i = 0
    
    while i < times:
        randInt1 = random.randrange(0, len(list))
        randInt2 = random.randrange(0, len(list))
        if randInt1 < randInt2:
            list[randInt2:len(list)], list[randInt1:randInt2] = list[randInt1:randInt2], list[randInt2:len(list)]
            i += 1
        else:
            list[randInt1:len(list)], list[randInt2:randInt1] = list[randInt2:randInt1], list[randInt1:len(list)]
            i += 1
    return list  

def bubbleSort(playerList):
    swapped = False
    for j in range(len(playerList)):
        for i in range(len(playerList) - j - 1):
            if playerList[i].sum_blackjack() > playerList[i + 1].sum_blackjack():
                playerList[i], playerList[i + 1] = playerList[i + 1], playerList[i]
                swapped = True
                
        if swapped == False:
            return playerList
                
def check_over_21(playerList):
    for i in playerList:
        if i.sum_blackjack() > 21:
            playerList.remove(i)
            playerList.append(i)

def check_ace(playerObject):
        for i in playerObject.cards:
            if int(i.number) == 1:
                    if i.blackjack_value == 11:
                        if playerObject.sum_blackjack() > 21:
                            i.blackjack_value = 1
                        else:
                            i.blackjack_value = 11
                        

def blackjack(deck, players):
    playerList = [] #To iterate through the player objects
    continueList = [] #Used for checking if all players are done with their cards
    i = 0 #iterate through amount of players
    x = 0 #card to be dealt
    y = 0 #var for first deal loop
    n = 0 #Used for player place
    
    playerList.append(player("Dealer", [])) #Holds dealers cards
    continueList.append(0)
    
    while i < (players - 1): #Holds all players cards except dealer
        playerList.append(player(f"Player {i + 1}", []))
        continueList.append(0)
        i += 1
        
    i = 0
        
    #while True: #Game loop
    while y < 2:    
        for i in range(players): #Deals cards to all players
            playerList[i].cards.append(deck[x]) # deals card to every playerh
            x += 1 #Sets up next card in the pile
        y += 1
        
    
    
    while True:  
        for i in playerList:
            check_ace(i)
             
        print(playerList[0].cards[0].blackjack_value)
        print("x")
        print("\n")
        
        for i in range(1, players):
            for z in range(len(playerList[i].cards)):
                print(playerList[i].cards[z].blackjack_value)
            print(f"Sum: {playerList[i].sum_blackjack()}")
            print("\n")  
            
        
        
        for i in range(1, players): #Checks if all players except dealer wants a card
            ask = input("press 1 if you want to raise, press 0 if you don't want to ")
            if int(ask) == 1: #Adds card to player who wants a card
                playerList[i].cards.append(deck[x])
                x += 1
            else:
                continueList[i] = 1 #adds a check for the player who doesn't want a card
        
        if sum(continueList) == players - 1: #Checks if all players have passed
            break
        
            
    while True:
        if playerList[0].sum_blackjack() < 17: #Checks if dealer wants a card
            playerList[0].cards.append(deck[x])
            x += 1
            check_ace(playerList[0])
        else:
            break
                

    bubbleSort(playerList)
    playerList.reverse()
    check_over_21(playerList)
    
    for i in playerList:   
        n += 1 
        print(f"{n}. {i.player_number}, {i.sum_blackjack()}")
    
            
            
            
deck = genCards(amountCards)

#printDeck(deck, 52)

print(blackjack(shuffle(genCards(amountCards), int(y)), int(x) + 1))
    