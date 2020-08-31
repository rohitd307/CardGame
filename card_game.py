import random
  
def createDeck ():
    arr = []
    j = 1
    for i in range(4):
        for j in range(1,11):
            arr.append(j)
    return arr
 
def shuffleDeck (arr, n): 
    try:
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            arr[i],arr[j] = arr[j],arr[i] 
        return arr 
    except IndexError:
        return arr

def splitDeck(arr, n):
    half = n/2
    return arr[:half], arr[half:]

def drawCard(player1CardDrawPile, player2CardDrawPile, player1DiscardPile, player2DiscardPile):
    try:
        player1Card = player1CardDrawPile[0]
        pile1Length = len(player1CardDrawPile) + len(player1DiscardPile)
        print ("Player 1 ({} cards) : {}".format(pile1Length, player1Card))
        
        player2Card = player2CardDrawPile[0]
        pile2ength = len(player2CardDrawPile) + len(player2DiscardPile)
        print ("Player 2 ({} cards) : {}".format(pile2ength, player2Card))
        
        winnerCard = decideDraw(player1Card, player2Card)
        if winnerCard == player1Card:
            player1DiscardPile = stackDiscardPile(player1Card, player2Card, player1DiscardPile)
        else:
            player2DiscardPile = stackDiscardPile(player1Card, player2Card, player2DiscardPile)
        player1CardDrawPile, player2CardDrawPile = checkPile(player1CardDrawPile, player2CardDrawPile, player1DiscardPile, player2DiscardPile)
        return player1CardDrawPile, player2CardDrawPile
    except IndexError:
        displayResult(player1CardDrawPile, player2CardDrawPile)
    except:
        print("Some problem occured")

def checkPile(player1CardDrawPile, player2CardDrawPile, player1DiscardPile, player2DiscardPile):
    player1CardDrawPile.pop(0)
    player2CardDrawPile.pop(0)
    if len(player1CardDrawPile) == 0 and len(player1DiscardPile) != 0:
        player1CardDrawPile = changePile(player1DiscardPile, player1CardDrawPile)
        shuffleDeck(player1CardDrawPile, len(player1CardDrawPile))
        del player1DiscardPile[:]

    if len(player2CardDrawPile) == 0 and len(player2DiscardPile) != 0:
        player2CardDrawPile = changePile(player2DiscardPile, player2CardDrawPile)
        shuffleDeck(player2CardDrawPile, len(player2CardDrawPile))
        del player2DiscardPile[:]
    return player1CardDrawPile, player2CardDrawPile

def decideDraw (player1Card, player2Card):
    if (player1Card > player2Card):
        print("Player 1 wins this round")
        return player1Card
    else:
        print("Player 2 wins this round")
        return player2Card

def stackDiscardPile(player1Card, player2Card, discardPile):
    discardPile.append(player1Card)
    discardPile.append(player2Card)
    return discardPile
   
def changePile (discardPile, drawPile):
    drawPile = [None] * len(discardPile)
    for i in range(0, len(discardPile)):
        drawPile[i] = discardPile[i]
    return drawPile

def displayResult(player1CardDrawPile, player2CardDrawPile):
    if len(player1CardDrawPile) == 0:
        print ("\nPlayer 2 wins the game..!!\n")
    if len(player2CardDrawPile) == 0:
        print ("\nPlayer 1 wins the game..!!\n")
    del player1CardDrawPile[:]
    del player2CardDrawPile[:]


# Driver program to test above function.
arr = createDeck()
n = len(arr)

shuffleDeck(arr, n)
player1CardDrawPile, player2CardDrawPile = splitDeck(arr, n)
player1DiscardPile = []
player2DiscardPile = []

try:
    while len(player1CardDrawPile) != 0 or len(player2CardDrawPile) != 0:
        player1CardDrawPile, player2CardDrawPile = drawCard(player1CardDrawPile, player2CardDrawPile, player1DiscardPile, player2DiscardPile)
except TypeError as identifier:
    del player1CardDrawPile[:]
    del player2CardDrawPile[:]