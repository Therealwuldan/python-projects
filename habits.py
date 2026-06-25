from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///habits.db"

db = SQLAlchemy(app)

class Habit(db.Model):
    id = db.Column(db.Integer,primary_key = True )
    name = db.Column(db.String(60) )
    completed = db.Column(db.Boolean)
    date = db.Column(db.DateTime)

@app.route("/", methods=["GET","POST"])

def home():
    if request.method == "POST":
        habit_id = request.form["habit_id"]
        habit = Habit.query.get(habit_id)
        habit.completed = True
        db.session.commit()

    habit = Habit.query.all()
    return render_template("habits.html", habits = habit)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Habit.query.count()== 0:
            habits = [
                Habit(name = "Code for 1hr", completed = False, date = datetime.today()),
                Habit(name = "Work on startup", completed = False, date = datetime.today()),
                Habit(name = "Gym", completed = False, date = datetime.today()),
                Habit(name = "Math", completed = False, date = datetime.today()),
                Habit(name = "Read pages", completed = False, date = datetime.today()),
            ]
            db.session.add_all(habits)
            db.session.commit()
    app.run(debug=True)
