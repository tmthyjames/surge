from flask import Flask
from db import db

class Problem(db.Model):
    __tablename__ = 'problems'

    id = db.Column(db.Integer, primary_key=True)
    term1 = db.Column(db.Integer, nullable=False)
    term2 = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.Integer, nullable=False)
    submitted_answer = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String, nullable=False)
    dateof = db.Column(db.DateTime, nullable=False)
