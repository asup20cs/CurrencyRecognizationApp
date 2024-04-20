import requests

def convert_currency(amount, from_currency, to_currency):
  # Replace with the API endpoint URL for your chosen currency exchange rate API
  api_url = f"https://v6.exchangerate-api.com/v6/589c15e44937ad22a08c7dce/pair/{from_currency}/{to_currency}/{amount}"

  response = requests.get(api_url)

  if response.status_code == 200:
    data = response.json()
    print(data)
    # Assuming the API response structure provides a conversion rate
    converted_amount = data["conversion_result"]
    return converted_amount 
  else:
    return None