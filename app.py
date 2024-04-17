from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes.usuarioRouter import usuario_bp, usuario_bp2
from api.service import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:26031993@localhost/agendador"
# initialize the app with the extension
db.init_app(app)

app.register_blueprint(usuario_bp, url_prefix='/usuario')

with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


