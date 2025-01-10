import requests
from bs4 import BeautifulSoup

from notification import send_sms


def check_little_sleepies(product_id: str, collection: str):
    # URL of the page to scrape
    url = 'https://littlesleepies.com/products/' + product_id

    # Fetch the page content using requests
    response = requests.get(url)

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the product's stock status (assuming it's in a <span> with class 'stock-status')
    stock_status = soup.find('button', class_='Rise-add-to-cart-button').text

    if 'Sold Out' in stock_status:
        print(f"No stock - Little Sleepies - {collection}/{product_id}")
        return {"message": 'Product is out of stock.'}
    else:
        # send_sms(f"Product is in stock! Please go to {url}")
        print("Stock - Little Sleepies - {collection}/{product_id}")
        send_sms(f"Product is in stock! Please go to Little Sleepies - {product_id}")

def check_meyers(product_id: str):
    # URL of the page to scrape
    url = 'https://meyerhatchery.com/products/' + product_id

    # Fetch the page content using requests
    response = requests.get(url)

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the product's stock status (assuming it's in a <span> with class 'stock-status')
    stock_status = soup.find('div', class_='label__text').text

    if 'Sold out' in stock_status:
        print(f"No stock - Meyer - {product_id}")
        return {"message": 'Product is out of stock.'}
    else:
        # send_sms(f"Product is in stock! Please go to {url}")
        print(f"Stock - Meyer - {product_id}")
        send_sms(f"Product is in stock! Please go to Meyer Hatchery - {product_id}")