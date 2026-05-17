import requests
import json

API_KEY = "VB7U3C1K9TXOU0XV"


def get_news(Ticker):
     url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={Ticker}&apikey={API_KEY}'
     data = requests.get(url)
     return data.json()


def display_news(data):
    if "feed" not in data or not data["feed"]:
        print("Invalid ticker or API limit reached.\n")
        return

    headline = data["feed"]


    for x in headline[:7]:
        print(x["title"])
        print(x["source"])




while True:
    Ticker = input("Enter your ticker or Q to quit: ").upper()
    if Ticker == "Q":
        break
    try:
        data = get_news(Ticker)
        display_news(data)
    except:
        print("Something went wrong!")

