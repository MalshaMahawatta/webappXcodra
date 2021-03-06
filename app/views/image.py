__author__ = 'Dilini'
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
UPLOAD_FOLDER_OFFERS =  'D:/WebAppXcodra/webappXcodra/app/static/img/offers/'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


imagebp = Blueprint('imagebp', __name__, url_prefix='/offers')


@imagebp.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_OFFERS'], filename))
            return redirect(url_for('imagebp.upload_file',
                                    filename=filename))



        flash('added images sucessfully.', 'positive')
        return redirect(url_for('index'))
        return render_template('image.html', title='Upload Images')
