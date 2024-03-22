from currency_converter import CurrencyConverter
cc=CurrencyConverter()
def convert_currency(amount, from_currency, to_currency):
    return cc.convert(amount, from_currency, to_currency)
print(convert_currency(100, 'INR', 'USD'))


