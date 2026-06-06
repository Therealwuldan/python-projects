from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

    new_search = Search(city="Toronto")
    db.session.add(new_search)
    db.session.commit()

    all_searches = Search.query.all()
    for search in all_searches:
        print(search.city)

print("Database created!")