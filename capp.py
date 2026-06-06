import flask
from flask import request
import requests
from flask import Flask, render_template



capp = Flask(__name__)


API_KEY = "871c8de84aa7e276da0ab746"


def get_rate(user_base,user_target):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{user_base}/{user_target}"
        response = requests.get(url)
        return response.json()
    except:
        print("Network error - check your connection")
        return None


@capp.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        base = request.form["base"]
        target = request.form["target"]
        amount = request.form["amount"]

        data = get_rate(base,target)
        result = data["conversion_rate"] * float(amount)

        return render_template("chome.html", result=result)
    return render_template("chome.html")

if __name__ == "__main__":
    capp.run(debug=True)