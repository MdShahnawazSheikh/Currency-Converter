import requests

def convert(from_currency = str(), to_currency = str(), amount=float()):
    """ Converts one currency to another"""
    API_KEY = "htDhSZyQKjwA4LH5uUIHknw81DfXpVge"
    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency.upper()}&from={from_currency.upper()}&amount={amount}"
    except:
        return "INVALID REQUEST! Param1 = Str(), Param2 = Str(), Param3 = Int() or Float()"
    payload = {}
    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    return result["result"]