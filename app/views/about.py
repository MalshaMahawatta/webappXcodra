__author__ = 'Dilini'


import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db






# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
aboutbp = Blueprint('aboutbp', __name__, url_prefix='/about')



@aboutbp.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html', title='About')


