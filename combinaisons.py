from time import sleep
from iteration_utilities import duplicates

def uncomposedCards(LastDraw):
  cardsValue = []
  cardsColors = []
  for cartes in LastDraw:
    cardsValue.append(cartes.split("-")[0])
    cardsColors.append(cartes.split("-")[1])
  for e,i in zip(cardsValue, range(0,5)):
    try:
      cardsValue[i] = int(e)
    except:
      if e == "J":
        cardsValue[i] = 11
      elif e == "Q":
        cardsValue[i] = 12
      elif e == "K":
        cardsValue[i] = 13
      elif e == "A":
        cardsValue[i] = 14
      else:
        continue

  return cardsValue, cardsColors

def Combinaisons(LastDraw, bankroll, betPlayer):

  if QuinteFlushRoyale(LastDraw):
    print("Quelle chance incroyable ! Vous avez obtenu une Quinte Flush Royale ! Improbable !")
    bankroll = (bankroll-betPlayer)+(betPlayer * 250)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")


  elif QuinteFlush(LastDraw):
    print("Wow ! Vous avez eu une QuinteFlush !")
    bankroll = (bankroll-betPlayer)+(betPlayer * 50)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")

  elif square(LastDraw) == True:
    print("Vous avez fait un Carré ! Bravo !")
    bankroll = (bankroll-betPlayer)+(betPlayer * 25)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")


  elif Full(LastDraw) == True:
    print("Vous avez fait un Full")
    bankroll = (bankroll-betPlayer)+(betPlayer * 9)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")


  elif Flush(LastDraw) == True:
    print("Vous venez d'obtenir un Flush")
    bankroll = (bankroll-betPlayer)+(betPlayer * 6)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")

  elif Quinte(LastDraw) == True:
    print("Vous avez une Quinte")
    bankroll = (bankroll-betPlayer)+(betPlayer * 4)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")

  elif Brelan(LastDraw) == True:
    print("Vous avez obtenu un Brelan")
    bankroll = (bankroll-betPlayer)+(betPlayer * 3)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")

  elif doublePairs(LastDraw) == True:
    print("Vous avez une double paire ! Vous remportez deux fois la mise")
    bankroll = (bankroll-betPlayer)+(betPlayer * 2)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")
  
  elif Pairs(LastDraw) == True:
    print("Vous avez obtenu une paire ! Vous remportez  votre mise")
    bankroll = (bankroll-betPlayer)+(betPlayer * 1)
    sleep(1)
    print("Le gain  a été crédité sur votre compte. Vous avez maintenant " + str(bankroll) + "€ sur votre compte")
  else:
    print("Désolé, Vous n'avez rien gagné ! Vous aurez plus de chance la prochaine fois")
    bankroll = bankroll - betPlayer 
    sleep(1.5)
  
  return bankroll


def Pairs(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)
  if bool(list(duplicates(cardsValue))) == True and len(list(duplicates(cardsValue))) == 1:
    
    return True
  else:
    return False


def doublePairs(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)
  listPairs = []
  listPairs = list(duplicates(cardsValue))
  
  if len(listPairs) == 2:
   
    return True
  else:
    return False


def Brelan(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)
  for i in cardsValue:
    if cardsValue.count(i) == 3:
      return True
  
  return False

def Quinte(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)
  cardsValue.sort()
  testingList = list(range(cardsValue[0], cardsValue[4]+1))
  if cardsValue == testingList:
    return True
  else: 
    return False

def Flush(LastDraw):
  no, cardsColors = uncomposedCards(LastDraw)
  for i in cardsColors:
    if cardsColors.count(i) == 5:
      return True
    else:
      return False
    
def Full(LastDraw):
  if Pairs(LastDraw) == True and Brelan(LastDraw) == True:
    return True
  else: 
    return False

def square(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)

  for i in cardsValue:
    if cardsValue.count(i) == 4:
      return True
    else: 
      return False

def QuinteFlush(LastDraw):

  if Quinte(LastDraw) == True and Flush(LastDraw) == True:
    return True
  else:
    return False

def QuinteFlushRoyale(LastDraw):
  cardsValue, no = uncomposedCards(LastDraw)
  cardsValue.sort()
  if cardsValue[0] == 10 and QuinteFlush(LastDraw) == True:
    return True
  else:
    return False