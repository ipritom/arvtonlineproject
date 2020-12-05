#Data Model for MongoDB 
##########################
from flask import Flask, jsonify, request
from passlib.hash import sha256_crypt
import uuid

class User:
    def signup(self):
        print("here",request.form) #check
        # Create the user object
        user = { 
                "_id": uuid.uuid4().hex,
                "firstName": request.form.get('firstName'),
                "lastName": request.form.get('lastName'),
                "email":  request.form.get('email'),
                "password": sha256_crypt.hash(request.form.get('password')),
                "userInfo":{
                    "gender": request.form.get('gender'),
                    "country": request.form.get('country'),
                    "countryByIp":""
                }
                }
        return user
