#Data Model for MongoDB 
##########################
from flask import Flask, jsonify, request
from passlib.hash import sha256_crypt
import uuid
import json
import requests

def checkCountry():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    url = "https://freegeoip.app/json/"+ip
    response = requests.request("GET", url, headers=headers)

    ipData = json.loads(response.text)

    return ipData['country_name']
    ########
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
                    "countryByIp":checkCountry()
                }
                }
        return user
