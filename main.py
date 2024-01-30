from flask import Flask
from admin.models import db
from admin.models import users
from datetime import timedelta
from admin.app import app
from settings.settings import third
from channels.channel import fourth
from flask_login import LoginManager
from flask_migrate import Migrate

second = Flask(__name__)
second.secret_key = "lovely29"
second.permanent_session_lifetime = timedelta(days=1)
second.app_context().push()



UPLOAD_FOLDER = 'admin/static/images/'

second.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
second.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
second.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


login_manager = LoginManager()
login_manager.init_app(second)
login_manager.login_view = 'app.login'
@login_manager.user_loader
def load_user(get_id):
    return users.query.get(int(get_id))

db.init_app(second)

migrate = Migrate(second, db)

second.register_blueprint(app, url_prefix='/admin')
second.register_blueprint(third, url_prefix='/admin/settings')
second.register_blueprint(fourth, url_prefix='/admin/channels')


if __name__ == "__main__":
    db.create_all()
    second.run(debug=True)