import requests

source = input("What currency do you want to convert from? Three characters.")
currencies = input("What currency do you want to convert to? Only one.")
date = input("What date do you want the exchange rate for? YYYY-MM-DD format.")

url = f"https://api.apilayer.com/exchangerates_data/{date}?symbols={currencies}&base={source}"

print(url)

payload = {}
headers= {
  "apikey": "sxdhjQkYt68QqyxqAVq0TmgnoOkfrXjg"
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response)


status_code = response.status_code
result = response.json()

if 'rates' in result and currencies in result['rates']:
    rate = result['rates'][currencies]
    print(f"Exchange rate on {date} is:\n")
    print(rate)
else:
    print("Error: Unable to retrieve the exchange rate.")
    print("Response content:", result)