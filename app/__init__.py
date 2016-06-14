from flask import Flask

from flask import send_from_directory



UPLOAD_FOLDER = 'G:/project 1/webappXcodra/app/static/img'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])


app = Flask(__name__)

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

from app.views import main, user, error,room, offers,image,gallery,facility,imageFacility
app.register_blueprint(user.userbp)
app.register_blueprint(room.roombp)
app.register_blueprint(offers.offersbp)
app.register_blueprint(image.imagebp)
app.register_blueprint(gallery.gallerybp)
app.register_blueprint(facility.facilitybp)
app.register_blueprint(imageFacility.imageFacilitybp)



# Setup the user login process
from flask.ext.login import LoginManager
from app.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'userbp.signin'


@login_manager.user_loader
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