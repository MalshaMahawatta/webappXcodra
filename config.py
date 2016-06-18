# DEBUG has to be to False in a production enrironment for security reasons
DEBUG = True
# Secret key for generating tokens
SECRET_KEY = 'houdini'
# Admin credentials
ADMIN_CREDENTIALS = ('ddrwijethunge@gmail.com', 'malsha')
# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'malshaforgdg@gmail.com'
MAIL_PASSWORD = ''
ADMINS = ['flask.boilerplate@gmail.com']
# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12


from flask import send_from_directory

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = 'D:/WebAppXcodra/webappXcodra/app/static/img/'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

