import random


class PokerCard():
    graph = ["tile","heart","clover","pike"]
    def getCard(self):
        myCards = []
        for i in range(3):
            myCards.append((random.randint(1, 13),self.graph[random.randint(0,3)]))
        return myCards



def showCard(aList):
    for index in range(len(aList)):
        aCard = aList[index]
        if aCard[0]<=10 and aCard[0]>=2:
            print "Card:",aCard[0],aCard[1]
        if aCard[0]==11:
            print "Card: J",aCard[1]
        if aCard[0]==12:
            print "Card: Q",aCard[1]
        if aCard[0]==13:
            print "Card: K",aCard[1]
        if aCard[0]==1:
            print "Card: A",aCard[1]
    return

def judge(cardListX,cardListY):
    return

def checkForDouble(cardList):
    cardList.sort()
    for index in range(len(cardList)-1):
        found = False
        if cardList[index]==cardList[index+1]:
            found == True
            return (cardList[index],cardList[index+1])
    return

def checkForTriple(cardList):
    if cardList[0]==cardList[1]==cardList[2]:
        return (cardList[0],cardList[1].cardList[2])
    return

def checkForGoldFlower(cardList):
    return

def checkForContinue(cardList):
    return

newPoker = PokerCard()
p1Cards = newPoker.getCard()
robotCards = newPoker.getCard()
print("Your cards: ")
showCard(p1Cards)
print("The robot's cards: ")
showCard(robotCards)
p = checkForDouble(p1Cards)
print p




