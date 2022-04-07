from combinaisons import Combinaisons
from Machine import Machine, firstDraw
from time import sleep
from flask import Flask, render_template, url_for, request, session, redirect
from Machine import *



deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']


app = Flask(__name__)
app.secret_key = "key"

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def start():
  age = int(request.form['age'])


  if age < 18:
      session['error-form'] = "Désolé vous n'avez pas l'âge légal requis."
      return render_template('index.html')
  else:  
      session['Banque'] = int(request.form['Banque'])
      return redirect(url_for('gamer'))

@app.route("/game")

def gamer():
  return render_template("game.html")


@app.route('/game', methods=['POST'])

def game():

  session['Bet'] = int(request.form["Bet"])
  if session['Bet'] > session['Banque']:
    session ['error-message'] = "Désolé mais votre mise est supérieure à l'argent sur votre compte"
    return render_template('game.html')
  else:
    session["newBanque"] = session["Banque"] - session["Bet"]
    drawed_cards, newDeck  = firstDraw(deck)
    session["drawed_cards"] = drawed_cards
    session["deck"] = newDeck
    

    return redirect(url_for('draw'))


@app.route('/tirage')  
def draw():

  return render_template("draw.html")
  

@app.route('/tirage', methods=['POST'])  
def Secondraw():
    LastDraw = session['drawed_cards']

    for card in request.form:
      LastDraw.remove(card)
    LastDraw = secondDraw(LastDraw, session['deck'])
    session['drawed_cards'] = LastDraw

    return redirect(url_for("result"))



@app.route('/result')

def final():
  return render_template('finalFile.html')



@app.route('/result')
def result():

  


  return render_template("finalFile.html")





if __name__ == '__main__':
  app.run(debug = True)





#On créer une variable qui contient les 52 cartes


#     while True:
#     
#         betPlayer = int(input("Combien voulez-vous miser pour le poker ?\n"))

#         while betPlayer > bankroll :

#           print("Désolé votre mise est supérieur à l'argent disponible sur votre compte. Veuillez réessayer.")
#           betPlayer = int(input("Combien voulez-vous miser pour le poker ?\n"))
#           break

#         if betPlayer <= bankroll:
#             print("Mise acceptée ! Bon jeu à vous !")
#             sleep(1.5)
#           #on lance nos fonctions
            
#             returnSecondDraw = Machine(deck)

#             bankroll = Combinaisons(returnSecondDraw, bankroll, betPlayer)
#             if bankroll <= 0:
#               print("Désolé, vous n'avez plus d'argent sur votre compte")
#               break
#             else:
#                 replay = int(input("Voulez vous rejouer ? Tapez 1 pour oui ou 0 pour quitter ?\n"))
#             if replay == 0:
#                 print("Vous récupérez " + str(bankroll) + "€, au revoir et à la prochaine !")
#                 exit()
# start()