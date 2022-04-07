import random
from random import sample
from time import sleep



deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

def Machine(deck):
  draw1 = firstDraw(deck)
  sleep(0.25)
  returnDeckChoice = deckChoice(draw1)
  sleep(0.25)
  returnSecondDraw = secondDraw(returnDeckChoice, deck)
  sleep(0.15)
  print("Vérification en cours... Veuillez patientez")
  sleep(0.5)

  return returnSecondDraw

def firstDraw(deck):

  random.shuffle(deck)
  drawed_cards = sample(deck, 5)
  print("Voici votre premier tirage :")
  sleep(1)
  print(drawed_cards)
  
  for i in drawed_cards:
    deck.remove(i)
    
  
  return drawed_cards

def deckChoice(drawed_cards):
  print("Que voulez-vous faire ?")
  
  newDeck = []
  for i in drawed_cards:
    
    choicePlayer = str(input("Voulez-vous garder " + i + " ? Dites oui ou non.\n"))
    if choicePlayer.lower() == "oui" or choicePlayer.lower() == "o":
      newDeck.append(i)
      sleep(0.5)
  return newDeck

def secondDraw(newDeck, deck):

  remainingCards = len(newDeck)
  LastDraw = []
  if remainingCards == 5:
    LastDraw = newDeck.copy()
    print("Voici votre tirage final : ")
    sleep(1.5)
    print(LastDraw)

  elif remainingCards == 4:
    LastDraw = newDeck.copy()
    LastDraw.extend(sample(deck, 1))
    print("Voici votre tirage final : ")
    sleep(1.5)
    print(LastDraw)

  elif remainingCards == 3:
      LastDraw = newDeck.copy()
      LastDraw.extend(sample(deck, 2))
      
      print("Voici votre tirage final : ")
      sleep(1.5)
      print(LastDraw)
  elif remainingCards == 2:
        LastDraw = newDeck.copy()
        LastDraw.extend(sample(deck, 3))
        print("Voici votre tirage final : ")
        sleep(1.5)
        print(LastDraw)
  elif remainingCards == 1:
         LastDraw = newDeck.copy()
         LastDraw.extend(sample(deck, 4))
         print("Voici votre tirage final : ")
         sleep(1.5)
         print(LastDraw)
  else:
    LastDraw = newDeck
    print("Voici votre tirage final : ")
    LastDraw.extend(sample(deck, 5))
    sleep(1.5)
    print(LastDraw)

  return LastDraw