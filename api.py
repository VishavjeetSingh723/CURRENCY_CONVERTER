import requests
import currency
import frtankfurter

FRANKFURTER_BASE_URL = 'https://www.frankfurter.app/'

def get_currency_codes():
    """
    Fetches the list of available currency codes from Frankfurter API.
    Returns a dictionary of currency codes and their names.
    """
    try:
        response = requests.get(f'{FRANKFURTER_BASE_URL}/currencies')
        if response.status_code == 200:
            return response.json()
        else:
            return {}
    except Exception as e:
        print(f"Error fetching currency codes: {e}")
        return {}

def get_latest_rate(base_currency, target_currency):
    """
    Fetches the latest conversion rate for the specified currency codes.
    Returns the conversion rate.
    """
    try:
        response = requests.get(f'{FRANKFURTER_BASE_URL}/{base_currency}/{target_currency}')
        if response.status_code == 200:
            data = response.json()
            return data.get(target_currency)
        else:
            return None
    except Exception as e:
        print(f"Error fetching latest conversion rate: {e}")
        return None

def get_historical_rate(date, base_currency, target_currency):
    """
    Fetches the historical conversion rate for the specified date and currency codes.
    Returns the conversion rate.
    """
    try:
        formatted_date = date.strftime('%Y-%m-%d')
        response = requests.get(f'{FRANKFURTER_BASE_URL}/{formatted_date}/{base_currency}/{target_currency}')
        if response.status_code == 200:
            data = response.json()
            return data.get(target_currency)
        else:
            return None
    except Exception as e:
        print(f"Error fetching historical conversion rate: {e}")
        return None
