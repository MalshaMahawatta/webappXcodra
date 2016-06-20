__author__ = 'Raditha'
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import facility as facility_details
from app.forms import imageFacility as facilityImage_details

UPLOAD_FOLDER = 'G:/project 1/webappXcodra/app/static/img/facilities'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
facilitybp = Blueprint('facilitybp', __name__, url_prefix='/facility')


@facilitybp.route('/addFacility', methods=['GET', 'POST'])
@login_required
def addFacility():
    form = facility_details.Facilities()
    if form.validate_on_submit():
        facility = models.Facility(
            facilityId=form.facilityId.data,
            facility=form.facility.data,
            description=form.description.data,

        )

        facility1 = models.Facility.query.filter_by(facilityId=form.facilityId.data).first()
        facility1.facility=form.facility.data
        db.session.commit()

        facility1.description=form.description.data
        db.session.commit()


        # Insert the facility in the database
        # db.session.add(facility)
        # db.session.commit()

        flash('added facility details sucessfully.', 'positive')
        return redirect("http://127.0.0.1:5000/facility/addImage")
    return render_template('facility/addfacility.html', form=form, title='facility Details')


@facilitybp.route('/showFacilities', methods=['GET', 'POST'])
@login_required
def showFacilities():
    facilities = models.Facility.query.all()
    return render_template('facility/showDetails.html', title='Facility', facilities=facilities)

@facilitybp.route('/addImage', methods=['GET', 'POST'])
def upload_file():
    form = facilityImage_details.FacilityImage()
    if form.validate_on_submit():

        image = form.image.data
        print image
        imageNew = str(image) + ".jpg"
        print imageNew

        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            print file.filename
            # if user does not select file, browser also
            # submit a empty part without filename
            file.filename = str(image) + ".jpg"
            print file.filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('facilitybp.upload_file',
                                        filename=filename))

                flash('added images sucessfully.', 'positive')
                return redirect(url_for('index'))
    return render_template('facility/addImage.html', form=form, title='Upload Images')





# @facilitybp.route('/showFacilities', methods=['GET', 'POST'])
# @login_required
# def showFacilities():
#     facilities = models.Facility.query.all()
#     # return render_template('facility/showDetails.html', title='Facility', facilities=facilities)