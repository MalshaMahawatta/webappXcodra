__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import facility as facility_details

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
            facility=form.facility.data,
            description=form.description.data,


        )
        # Insert the facility in the database
        db.session.add(facility)
        db.session.commit()

        flash('added facility details sucessfully.', 'positive')
        return redirect(url_for('addImage'))
    return render_template('facility/details.html', form=form, title='facility Details')



@facilitybp.route('/showFacilities',methods=['GET', 'POST'])
@login_required
def showFacilities():
    facilities=models.Facility.query.all()
    return render_template('facility/showDetails.html', title='Facility',facilities=facilities)






