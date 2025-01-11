import requests

from config import TEXTBELT_API_KEY


def send_sms(body: str, phone_number: str):
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': body,
        'key': TEXTBELT_API_KEY,
    })
    print(resp.json())
    # print("Triggered SMS")