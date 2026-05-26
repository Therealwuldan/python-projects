import flask
import requests
from flask import Flask, render_template
from flask import request




app = Flask(__name__)

API_KEY = "065f489cb0f1a39404103d9d561f3f4b"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    responses = requests.get(url)
    return responses.json()

@app.route("/", methods = ["GET","POST"])
def home():

    if request.method == "POST":
        city = request.form["city"]
        data = get_weather(city)


        return render_template("home.html", weather=data)

    return render_template("home.html")  # runs on GET, shows empty form

if __name__ == "__main__":
    app.run(debug=True)
