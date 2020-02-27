#-*-coding:utf-8 -*-
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # implement required property and methods for Flask-Login.
# Property: is_authenticated, is_active,is_anonymous. Methods: get_id()


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Point (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    pointname = db.Column(db.String(64), index=True, unique=True)
    volt1 = db.Column(db.String(64), index=False, unique=False)
    volt2 = db.Column(db.String(64), index=False, unique=False)
    temp = db.Column(db.String(64), index=False, unique=False)
    load1 = db.Column(db.String(64), index=False, unique=False)
    load2 = db.Column(db.String(64), index=False, unique=False)
    load3 = db.Column(db.String(64), index=False, unique=False)
    digInA = db.Column(db.String(64), index=False, unique=False)
    digInB = db.Column(db.String(64), index=False, unique=False)
    digInC = db.Column(db.String(64), index=False, unique=False)
    digInD = db.Column(db.String(64), index=False, unique=False)
    date = db.Column(db.String(256), index=False, unique = False)
    modulName = db.Column(db.String(256), index=False, unique = False)

    data = db.relationship('Data', backref='author', lazy='dynamic')

    def __init__(self,name=None,V1=None,V2=None,T=None,ld1="0",ld2="0",ld3="0",A="0",B="0",C="0",D="0"):
        self.pointname = name
        self.volt1 = V1
        self.volt2 = V2
        self.temp = T
        self.load1 = ld1
        self.load2 = ld2
        self.load3 = ld3
        self.digInA = A
        self.digInB = B
        self.digInC = C
        self.digInD = D

    def __repr__(self):
        return '<Point {},{},{},{},{},{},{},{},{},{},{} >'.format(
            self.pointname,self.volt1,self.volt2,self.temp,
            self.load1,self.load2,self.load3,
            self.digInA,self.digInB,self.digInC,self.digInD) 

    def get(self,attr):
        return object.__getattribute__(self,attr)

    def setAttr(self,attr,value):
        return object.__setattr__(self,attr,value)

    def setPoint(self, PointName):
       self.pointname  = PointName

    def getPoint(self):
        return self.pointname

    def getId(self):
        return self.id


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voltage = db.Column(db.String(140))
    temperature = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    point_id = db.Column(db.Integer, db.ForeignKey('point.id'))

    def __repr__(self):
        return '<Data: {} V {} C>'.format(self.voltage,self.temperature)
    
    def setVoltage(self,value):
        self.voltage = value

    def getVoltage(self):
        return self.voltage

    def setTemperature(self,value):
        self.temperature = value
    
    def getTemperature(self):
        return self.temperature
