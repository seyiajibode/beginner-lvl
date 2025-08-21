import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert(amount, from_currency, to_currency):
    try:
        response = requests.get(API_URL)
        data = response.json()
        rates = data["rates"]

        if from_currency not in rates or to_currency not in rates:
            print("Invalid currency code.")
            return

        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]
        print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., EUR): ").upper()
    convert(amount, from_curr, to_curr)
