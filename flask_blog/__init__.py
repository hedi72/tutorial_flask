from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# create secret key
# app.secret_key = "26ce5cd11062e391679604ecfb045e68"

app.config['SECRET_KEY'] = '26ce5cd11062e391679604ecfb045e68'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



from flask_blog import routes

