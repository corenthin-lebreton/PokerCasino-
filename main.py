from combinaisons import Combinaisons
from Machine import *
from flask import Flask, render_template, url_for, request, session, redirect


app = Flask(__name__)
app.secret_key = "key"

@app.route('/')

def index():
  return render_template("index.html")

@app.route('/', methods=['POST'])
def start():
  age = int(request.form['age'])


  if age < 18:
      session['error-form'] = "Ce n'est pas un lieu pour les gamins !"
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