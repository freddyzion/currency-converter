import os
import requests
from dotenv import load_dotenv
# from index import BASE_URL

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "EUR", "GBP", "JPY", "AUD", "CHF", "CNY", "SEK", "NZD"]

def convertCurrency(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={','.join(CURRENCIES)}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        return e
    
userCurrency = input("Choose a currency (e.g., USD, CAD, EUR): ").upper()
data = convertCurrency(userCurrency)

try:
    for currency, rate in data.items():
        print(f"1 {userCurrency} = {rate} {currency}")
except Exception as e:
    print(f"We don't support {userCurrency}. Please try again with a different currency.")