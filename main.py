from flask import Flask, render_template

from game import GameOfLife

app = Flask(__name__)


@app.route('/')
def main():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    
    return render_template('live.html', life=life)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)