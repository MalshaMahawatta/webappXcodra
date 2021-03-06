from flask import Flask


from flask import send_from_directory


UPLOAD_FOLDER = 'D:/Xcodra/webappXcodra/app/static/img/offers'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])






UPLOAD_FOLDER_GALLERY = 'D:/WebAppXcodra/webappXcodra/app/static/img/gallery/'
UPLOAD_FOLDER_OFFERS = 'D:/WebAppXcodra/webappXcodra/app/static/img/offers/'
UPLOAD_FOLDER_FACILITIES = 'D:/WebAppXcodra/webappXcodra/app/static/img/facilities/'



ALLOWED_EXTENSIONS = set(['jpeg','png','jpg'])
app = Flask(__name__)
from flask import send_from_directory

# Setup the app with the config.py file
app.config.from_object('config')

# Setup the database
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Setup the mail server
from flask.ext.mail import Mail

mail = Mail(app)

# Setup the password crypting
from flask.ext.bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# Import the views

from app.views import main, user, error,room,offers,image,gallery,guest,viewGuest,facility,about,feedback

app.register_blueprint(user.userbp)
app.register_blueprint(room.roombp)
app.register_blueprint(gallery.gallerybp)
app.register_blueprint(offers.offersbp)
app.register_blueprint(guest.guestbp)
app.register_blueprint(viewGuest.viewGuestbp)
app.register_blueprint(facility.facilitybp)
app.register_blueprint(about.aboutbp)
app.register_blueprint(feedback.feedBackbp)





from app.toolbox import RecognizedCustomer


# Setup the user login process
from flask.ext.login import LoginManager
from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'userbp.signin' \

@ login_manager.user_loader


def load_user(email):
    return User.query.filter(User.email == email).first()


# Setup the admin interface
from flask import request, Response
from werkzeug.exceptions import HTTPException
from flask_admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import LoginManager
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op

import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

admin = Admin(app, name='Admin', template_mode='bootstrap3')


class ModelView(ModelView):
    def is_accessible(self):
        auth = request.authorization or request.environ.get('REMOTE_USER')  # workaround for Apache
        if not auth or (auth.username, auth.password) != app.config['ADMIN_CREDENTIALS']:
            raise HTTPException('', Response('You have to an administrator.', 401,
                                             {'WWW-Authenticate': 'Basic realm="Login Required"'}
                                             ))
        return True


# Users
admin.add_view(ModelView(User, db.session))
# Static files
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static'))
