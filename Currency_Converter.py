import requests

url = 'https://api.exchangerate-api.com/v4/latest/USD'

response = requests.get(url)

data = response.json()

print("Welcome to the Currency Converter")
print("Available currencies:")

for currency in data['rates']:
    print(currency)

from_currency = input("From which currency would you like to convert? ")
to_currency = input("To which currency would you like to convert? ")
amount = float(input(f"How much {from_currency} do you want to convert? "))

conversion_rate = data['rates'][to_currency] / data['rates'][from_currency]
converted_amount = amount * conversion_rate

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")