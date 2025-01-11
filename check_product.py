import re

import requests
from bs4 import BeautifulSoup

from config import SEND_SMS_TO
from notification import send_sms


def check_little_sleepies(product_id: str, collection: str):
    # URL of the page to scrape
    url = 'https://littlesleepies.com/products/' + product_id

    # Fetch the page content using requests
    response = requests.get(url)

    if is_sold_out(response.text):
        print(f"No stock - Little Sleepies - {collection}/{product_id}")
        return {"message": 'Product is out of stock.'}
    else:
        # send_sms(f"Product is in stock! Please go to {url}")
        print("Stock - Little Sleepies - {collection}/{product_id}")
        send_sms(f"Product is in stock! Please go to Little Sleepies - {product_id}", SEND_SMS_TO)

def check_meyers(product_id: str):
    # URL of the page to scrape
    url = 'https://meyerhatchery.com/products/' + product_id

    # Fetch the page content using requests
    response = requests.get(url)

    if is_sold_out(response.text):
        print(f"No stock - Meyer - {product_id}")
        return {"message": 'Product is out of stock.'}
    else:
        # send_sms(f"Product is in stock! Please go to {url}")
        print(f"Stock - Meyer - {product_id}")
        send_sms(f"Product is in stock! Please go to Meyer Hatchery - {product_id}", SEND_SMS_TO)

def is_sold_out(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # This will match variations like "SOLD OUT", "Sold-Out", "SoldOut", etc.
    pattern = re.compile(r'sold[\s-]*out', re.IGNORECASE)
    return bool(pattern.search(soup.text))