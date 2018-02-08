from flask import Flask, render_template, json, request, redirect, session
from flask_ask import Ask, request, session, question, statement
from werkzeug import generate_password_hash, check_password_hash
import os
import re
import requests



app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showSignin')
def showSignin():
     if session.get('user'):
         return render_template('userHome.html')
     else:
         return render_template('signin.html')

@app.route('/showAddWish')
def showAddWish():
    return render_template('addWish.html')

################### ALEXA SKILLS SECTION #####################

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    return question(help_text).reprompt(help_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return "{}", 200




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5002)
