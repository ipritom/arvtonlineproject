from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from passlib.hash import sha256_crypt
from arvtonline.extensions import mongo

admin = Blueprint('admin',__name__,url_prefix='/admin',template_folder="templates/admin")

def isAdmin():
    return True

@admin.route('/')
def index():
    if isAdmin:
        return render_template("admin.html")
    else:
        return redirect(url_for('site.index'))

@admin.route('/set_questions')
def set_questions():
    if isAdmin:
        return render_template("set_questions.html")
    else:
        return redirect(url_for('site.index'))
@admin.route('/users')
def users():
    if isAdmin:
        colleclion = mongo.db.users
        users = colleclion.find({})
        return render_template("admin_users.html",users=users)
    else:
        return redirect(url_for('site.index'))
