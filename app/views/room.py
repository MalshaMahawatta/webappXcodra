__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import room as room_details
from flask_table import Table, Col


# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
roombp = Blueprint('roombp', __name__, url_prefix='/room')

@roombp.route('/addRoom', methods=['GET', 'POST'])
@login_required
def addRoom():
    form = room_details.Rooms()
    if form.validate_on_submit():
        type=form.type.data
        print(type)
        if int(type) is 1:

            room = models.Room(


            number=form.number.data,
            type="superior",
            roomPrice=75000,
            availability=True,



        )
        elif int(type)==2:
            room = models.Room(


            number=form.number.data,
            type="Delux",
            roomPrice=50000,
            availability=True,



             )

        else:
            room = models.Room(


            number=form.number.data,
            type="Standard",
            roomPrice=25000,
            availability=True,


             )
                # Insert the room in the database
        db.session.add(room)
        db.session.commit()

        flash('added room details sucessfully.', 'positive')
        return redirect(url_for('index'))
    return render_template('room/details.html', form=form, title='Room Details')


@roombp.route('/showRooms', methods=['GET', 'POST'])
@login_required
def showRooms():

    rooms = models.Room.query.all()
    class ItemTable(Table):
        classes = ['ui celled table']
        number = Col('number')
        type = Col('type')
        availability = Col('availability ')
        guest_number = Col('guest_number ')

    table = ItemTable(rooms)
    #print(table.__html__())
    return render_template('room/showDetails.html', title='Room', rooms=table)

