import requests

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = response.json()

print("The price of Bitcoin:", data["bitcoin"]["usd"], "USD")
