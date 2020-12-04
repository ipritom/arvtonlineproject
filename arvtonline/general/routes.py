from flask import Blueprint, request, render_template, redirect, url_for
from arvtonline.extensions import mongo
from .models import User

site = Blueprint('site',__name__,template_folder='templates')

@site.route('/')
def index():
    return render_template('home.html')

@site.route('/signup',methods=['POST','GET'])
def signup():
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
                print("An exception occurred ::", e)
                return render_template('signup.html')
            
    return render_template('signup.html')

@site.route('/login')
def login():
    return render_template('login.html')