"""
The purpose this file is to only get used to basics of FLASK commands.
The main file that we have used for our project is the 'app.py'.

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
