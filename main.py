from combinaisons import *
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

  session['error-form'] = False
  if age < 18:
      session['error-form'] = "Ce n'est pas un lieu pour les gamins !"
      return render_template('index.html')
  else:  
      session['Banque'] = int(request.form['Banque'])
      session['musique'] = 0
      return redirect(url_for('gamer'))

@app.route("/game")

def gamer():
  return render_template("game.html")


@app.route('/game', methods=['POST'])

def game():

  session['Bet'] = int(request.form["Bet"])
  session['error-message'] = False
  if session['Bet'] > session['Banque']:
    session ['error-message'] = "Désolé mais votre mise est supérieure à l'argent sur votre compte"
    return render_template('game.html')
  else:
    session['Banque'] = session["Banque"] - session["Bet"]
    drawed_cards, newDeck  = firstDraw(deck)
    session["drawed_cards"] = drawed_cards
    session["deck"] = newDeck
    session['musique'] = 64.1

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
    resultat, g = Combinaisons(session['drawed_cards'], session['Banque'], session['Bet'])

    session['result'] = resultat
    print(resultat, g)
    session['gain'] = g
    session['Banque'] = session['Banque'] + session['gain']
    session['musique'] = 85
    return redirect(url_for("result"))

@app.route('/result')
def final():
  return render_template('finalFile.html')



@app.route('/result', methods=['POST'])
def result():


  return render_template("finalFile.html")


if __name__ == '__main__':
  app.run(debug = True)