import requests

from config import TEXTBELT_API_KEY


def send_sms(body ):
    print(TEXTBELT_API_KEY)
    resp = requests.post('https://textbelt.com/text', {
        'phone': '4236502449',
        'message': body,
        'key': TEXTBELT_API_KEY,
    })
    print(resp.json())