#Data Models
from flask import Flask, jsonify, request
from passlib.hash import sha256_crypt
import uuid

class Questions:
    def set_question(self):
        question = {
            "_id" : uuid.uuid4().hex,
            "level" : request.form.get('level'),
            "weight" : request.form.get('weight'),
            "question" : request.form.get('question'),
            "options" : request.form.get('options')
        }
    
    def participations(self):
        participation = {
            "userID" : userID,
            "anwered" : {
                "qID": qID,
                "isCorrect": [True,False],
            },
            {},

        }