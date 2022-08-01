from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
  "apiKey": "AIzaSyBQ3uszrjXJTmMbRtR910reV1pHbZVAghk",
  "authDomain": "fir-authentication-lab-37df7.firebaseapp.com",
  "projectId": "fir-authentication-lab-37df7",
  "storageBucket": "fir-authentication-lab-37df7.appspot.com",
  "messagingSenderId": "136373746316",
  "appId": "1:136373746316:web:62f123fcc74a01f860d9a9",
  "databaseURL": ""
}

firebase =pyrebase.initialize_app (firebaseConfig)
auth = firebase.auth()


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method =='POST':
        email= request.form['email']
        password = request.form ['password']
        try:
            login_session['user'] = auth.signin_user_with_email_and_password(email,password)
        return redirect (url_for("add_tweet.html"))
    except:
        error = 'Signin Failed'
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email= request.form['email']
        password = request.form ['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
        return redirect (url_for("add_tweet.html"))
    except:
        error = 'Failed'
    return render_template('signup.html')


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)