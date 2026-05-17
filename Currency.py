import json

import requests


API_KEY = "871c8de84aa7e276da0ab746"


def get_rate(user_base,user_target):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{user_base}/{user_target}"
        response = requests.get(url)
        return response.json()
    except:
        print("Network error - check your connection")
        return None

def display_conversion(data, user_amount):
    result = data["conversion_rate"] * user_amount
    print(f"{user_amount} {user_base} = {result:.2f} {user_target}")


while True:
    user_base = input("Enter your base currency or 'q' to quit: ").upper()
    if user_base == "Q":
        break

    user_target = input("Enter your target currency: ").upper()
    user_amount = int(input("Enter your amount: "))

    data = get_rate(user_base,user_target)
    if data is None:
        continue
    if data["result"] == "error":
        print("Invalid currency code")
    else: display_conversion(data, user_amount)



