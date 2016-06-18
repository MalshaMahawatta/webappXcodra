__author__ = 'Raditha'
from flask import Flask, request
from flask_restful import Resource, Api ,reqparse
from app import app

api = Api(app)

class CustomerRecognized(Resource):
    def get(self):
       try:
        parser = reqparse.RequestParser()
        parser.add_argument('customerId', type=str, help='Customer id of the recognized customer')
        args = parser.parse_args()
        cusId=args['customerId']
        return {'Customer': args['customerId']}
       except Exception as e:
        return {'error': str(e)}
    def put(self):
        d = request.form['data']
        print(d)
        return {'data':'received(put)'}

api.add_resource(CustomerRecognized, '/sendCustomer')

