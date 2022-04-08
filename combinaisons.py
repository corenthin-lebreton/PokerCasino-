
from iteration_utilities import duplicates
<<<<<<< HEAD

=======
>>>>>>> c1f5fb85c73167ef24e8c934fd6864c0326706a8

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
    resultat = "Félicitation ! Vous avez obtenu une Quinte Flush Royale"
    g = betPlayer * 250
    return resultat,g

  elif QuinteFlush(LastDraw):
    resultat = "Bravo vous avez obtenu une Quinte Flush"
    g = betPlayer * 50
    return resultat, g

  elif square(LastDraw) == True:
    resultat = 'Bravo vous avez obtenu un carré'
    g = betPlayer * 25
    return resultat, g

  elif Full(LastDraw) == True:
    resultat = "Bravo vous avez obtenu un full"
    g = betPlayer * 9
    return resultat, g

  elif Flush(LastDraw) == True:
    resultat = "Bravo vous avez obtenu une Flush"
    g = betPlayer * 6
    return resultat, g

  elif Quinte(LastDraw) == True:
    resultat = "Bravo vous avez obtenu une Quinte"
    g = betPlayer * 4
    return resultat, g


  elif Brelan(LastDraw) == True:
    resultat = "Bravo vous avez obtenu un Brelan"
    g = betPlayer * 3
    return resultat, g

  elif doublePairs(LastDraw) == True:
    resultat = "Bravo vous avez obtenu une double paire"
    g = betPlayer * 2
    return resultat, g

  elif Pairs(LastDraw) == True:
    resultat = "Bravo vous avez obtenu une Paire"
    g = betPlayer * 1
    return resultat, g
  else:
    resultat = "Désolé vous n'avez aucune combinaisons gagnantes"
    return resultat, 0


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