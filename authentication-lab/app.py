from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBQ3uszrjXJTmMbRtR910reV1pHbZVAghk",
  "authDomain": "fir-authentication-lab-37df7.firebaseapp.com",
  "projectId": "fir-authentication-lab-37df7",
  "storageBucket": "fir-authentication-lab-37df7.appspot.com",
  "messagingSenderId": "136373746316",
  "appId": "1:136373746316:web:62f123fcc74a01f860d9a9"
}

firebase =pyrebase.initalize_app(firebaseConfig)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyBQ3uszrjXJTmMbRtR910reV1pHbZVAghk",
  "authDomain": "fir-authentication-lab-37df7.firebaseapp.com",
  "projectId": "fir-authentication-lab-37df7",
  "storageBucket": "fir-authentication-lab-37df7.appspot.com",
  "messagingSenderId": "136373746316",
  "appId": "1:136373746316:web:62f123fcc74a01f860d9a9"
}

firebase =pyrebase.initalize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)