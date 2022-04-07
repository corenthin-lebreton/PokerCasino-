from combinaisons import Combinaisons
from Machine import Machine
from time import sleep
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
    return redirect(url_for('draw'))


@app.route('/tirage')  
def draw():

  return render_template("draw.html")




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