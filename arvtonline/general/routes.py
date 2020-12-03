from flask import Blueprint, render_template

site = Blueprint('site',__name__,template_folder='templates')

@site.route('/')
def index():
    return render_template('home.html')

@site.route('/signup')
def signup():
    return render_template('signup.html')

@site.route('/login')
def login():
    return render_template('login.html')