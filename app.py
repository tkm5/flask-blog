from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# if you use TimeZone
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='localhost',
            debug=True)
