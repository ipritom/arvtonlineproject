from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from passlib.hash import sha256_crypt
from arvtonline.extensions import mongo
import requests
import json
from .models import User

site = Blueprint('site',__name__,template_folder='templates')

@site.route('/')
def index():
    if 'user._id' in session:
        print('INDEX MSG: LOGGED IN')
        return render_template('home.html',session=session)
    return render_template('home.html')

@site.route('/signup',methods=['POST','GET'])
def signup():
    if 'user._id' in session:
        return redirect(url_for('site.index'))
    if request.method == 'POST':
        users = mongo.db.users
        
        #checking the existence of the email in database
        isExist = users.find_one({'email':request.form['email']})

        if isExist is None:
            user = User().signup()
            try:
                mongo.db.users.insert_one(user)
                return redirect(url_for('site.login'))
            except Exception as e:
                print("An exception occurred ::", e) #system msg
                flash("An exception occurred! Please try again.")
                return redirect(url_for('site.signup'))
        else:
            flash("This Account Already Exist!")
            return redirect(url_for('site.signup'))
            
    return render_template('signup.html')

@site.route('/login',methods=['POST','GET'])
def login():
    if 'user._id' in session:
        return redirect(url_for('site.index'))

    if request.method == 'POST':
        user_email = request.form['email']
        user_pwd = request.form['password']

        #checking the existence of the email in database
        users = mongo.db.users
        isExist = users.find_one({'email':user_email})
        
        #process log in
        if isExist!=None:
            #verify user password
            user_pwd_hash = isExist['password']
            user_pwd_isCorrect = sha256_crypt.verify(user_pwd,user_pwd_hash)

            if user_pwd_isCorrect:
                session['user._id'] = isExist['_id']
                session['user.firstName'] = isExist['firstName']
                return redirect(url_for('site.index'))
            else:
                flash('Wrong Password! Please try again.')
                return redirect(url_for('site.login'))
        
        else:
            flash("This account doesn't exist. You can create an account with this email address.")
            return redirect(url_for('site.login'))

    return render_template('login.html')

@site.route('/profile',methods=['POST','GET'])
def profile():
    if 'user._id' in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('site.login'))

@site.route('/logout')
def logout():
    if 'user._id' in session:
        session.pop('user._id')
        return redirect(url_for('site.index'))
    else:
        return redirect(url_for('site.login'))