__author__ = 'Malsha'
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import gallery as gallery_details

UPLOAD_FOLDER = '/D:/WebAppXcodra/webappXcodra/app/static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


gallerybp = Blueprint('gallerybp', __name__, url_prefix='/gallery')


@gallerybp.route('/addImage', methods=['GET', 'POST'])
def upload_file():
    # image = request.form['image']
    form = gallery_details.Gallery()
    if form.validate_on_submit():

        image = form.image.data
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            file.filename = image
            print file.filename
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('gallerybp.upload_file',
                                        filename=filename))

                flash('added images sucessfully.', 'positive')
                return redirect(url_for('index'))
    return render_template('gallery/gallery.html', form=form, title='Upload Images')


@gallerybp.route('/showGallery', methods=['GET', 'POST'])
@login_required
def showGallery():
    return render_template('gallery/userGallery.html', title='Gallery')
