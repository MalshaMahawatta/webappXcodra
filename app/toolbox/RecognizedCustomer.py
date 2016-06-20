__author__ = 'Raditha'
from flask import Flask, request,flash,redirect,url_for
from flask_restful import Resource, Api, reqparse
from app import app,db,models
import datetime
import base64
import ctypes  # An included library with Python install.
api = Api(app)

class CustomerRecognized(Resource):
    def get(self):
       try:
        flash("got a customer",'positive')
        parser = reqparse.RequestParser()
        parser.add_argument('customerId', type=str, help='Customer id of the recognized customer')
        parser.add_argument('image',type=str,help='BASE64 Image')
        args = parser.parse_args()
        cusId = args['customerId']
        ctypes.windll.user32.MessageBoxA(0, "Customer "+cusId + " " +"is arriving", "Recognized Customer", 1)
        #recogedGuest = models.Guest.query.filter_by(number=cusId).first()
        #recogedGuest.arrivalTime = datetime.now()

        #recogedGuest.recognized=True
        #db.session.commit()
        img=args['image']
        print img

        return {'Customer': args['customerId'],'Image':args['image']}
       except Exception as e:
        return {'error': str(e)}
    def put(self):
        d = request.form['data']
        print(d)
        return {'data':'received(put)'}

api.add_resource(CustomerRecognized, '/sendCustomer')

