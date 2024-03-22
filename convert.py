from currency_converter import CurrencyConverter
cc=CurrencyConverter()
def convert_currency(amount, from_currency, to_currency):
    amount = cc.convert(amount, from_currency, to_currency)
    return amount