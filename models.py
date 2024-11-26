from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Chinh%4027@localhost/Login'
app.config['SECRET_KEY'] = '543460c80daec459ddd1e46d25bc2f2ad4f5a27cff20317e'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Tạo cơ sở dữ liệu và bảng
with app.app_context():
    db.create_all()