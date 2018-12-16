from flask import Flask ,session
import os

app = Flask(__name__)
app.secret_key= os.urandom(24)

@app.route('/')
def index():
    session['user'] = 'Anthony'
    return 'index'

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    else:
        return "not logged in"


@app.route('/droppedsession')
def dropsession():
    session.pop('user',None)
    return 'Dropped!'

if __name__=='__main__':
    app.run(debug=True)

