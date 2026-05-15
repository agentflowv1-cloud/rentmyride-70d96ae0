import requests
import json

class PaymentAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.stripe.com/v1'

    def process_payment(self, amount, currency, card_number, exp_month, exp_year, cvc):
        params = {
            'amount': amount,
            'currency': currency,
            'card[number]': card_number,
            'card[exp_month]': exp_month,
            'card[exp_year]': exp_year,
            'card[cvc]': cvc
        }
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(self.base_url + '/charges', params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def handle_errors(self, response):
        if response.status_code == 400:
            return 'Invalid request'
        elif response.status_code == 401:
            return 'Unauthorized'
        elif response.status_code == 500:
            return 'Internal server error'
        else:
            return 'Unknown error'
