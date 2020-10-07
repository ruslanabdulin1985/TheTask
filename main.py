from flask import Flask, render_template
from model.games import Games


app = Flask(__name__)

games = Games()

# api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/setup")
def setup():
    return render_template('setup.html')

@app.route("/game")
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0', ) #ssl_context='adhoc')
