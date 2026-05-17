import requests
import json


API_KEY = "VB7U3C1K9TXOU0XV"


def get_data(Ticker):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={Ticker}&apikey={API_KEY}"
    data = requests.get(url)
    return data.json()



def display(data):
    if 'Global Quote' not in data or not data['Global Quote']:
        print("Invalid ticker or API limit reached.\n")
        return
    print("\n--- STOCK DATA ---")
    print(f"Symbol: {data['Global Quote']['01. symbol']}")
    print(f"Price: {data['Global Quote']['05. price']}")
    print(f"Change: {data['Global Quote']['09. change']}")
    print(f"Percent change: {data['Global Quote']['10. change percent']}")





while True:
    try:
        Ticker = input("Enter your ticker (or q to quit): ").upper()
        if Ticker == "Q":
            break
        data = get_data(Ticker)
        display(data)

    except:
        print("Something went wrong re enter the ticker") #catches crashes w internet or sum befor it gets a response
#{'Global Quote': {'01. symbol': 'AAPL', '02. open': '279.6550', '03. high': '280.6300', '04. low': '274.8601', '05. price': '276.8300', '06. volume': '46668401', '07. latest trading day': '2026-05-04', '08. previous close': '280.1400', '09. change': '-3.3100', '10. change percent': '-1.1816%'}}
