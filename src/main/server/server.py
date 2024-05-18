from time import sleep
from flask import Flask
from src.main.routes.company import company_bp
from src.main.routes.contact import contact_bp
from src.main.database.database import db


app = Flask(__name__)
app.register_blueprint(company_bp)
app.register_blueprint(contact_bp)
app.config.from_pyfile('settings.py')
db.init_app(app)

with app.app_context():
    sleep(10)
    db.create_all()