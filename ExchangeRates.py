from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import json

load_dotenv()

exchange_rates = []

def initialize():
    '''
    Fetch HTML content from bank's website
    '''
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = os.getenv("EXCHANGE_RATES_URL")
    driver.get(url)

    html_content = driver.page_source
    
    driver.quit()
    
    return html_content

def get_exchange_rates(html_content):
    '''
    Parse HTML content to get exchange rates
    '''
    soup = BeautifulSoup(html_content, "html.parser")

    rows = soup.find_all('tr')

    for row in rows:
        currency_code_td = row.find('td', class_='col-1-3')
        if currency_code_td:
            currency_code = currency_code_td.get_text(strip=True)
            currency_name = row.find('td', class_='col-2-3 d-mobile-none').text.strip()
            prices = row.find_all('td', class_='col-1-5 text-end')
            if len(prices) >= 3:
                exchange_rate = {
                    'currency_code': currency_code,
                    'currency_name': currency_name,
                    'buy_price_cash': prices[0].text.strip(),
                    'buy_price_online': prices[1].text.strip(),
                    'sell_price': prices[2].text.strip()
                }
                exchange_rates.append(exchange_rate)

def display_exchange_rates(rates):
    """
    Display exchange rates in a readable format
    """
    for rate in rates:
        print(f"Mã tiền tệ: {rate['currency_code']}")
        print(f"Tên tiền tệ: {rate['currency_name']}")
        print(f"Giá mua tiền mặt: {rate['buy_price_cash']}")
        print(f"Giá mua chuyển khoản: {rate['buy_price_online']}")
        print(f"Giá bán: {rate['sell_price']}")
        print("-" * 50)

def get_new_exchange_rates():
    html_content = initialize()
    get_exchange_rates(html_content)
    return exchange_rates

def get_current_exchange_rates():
    return exchange_rates

def save_to_json():   
    with open('exchange_rates.json', 'w', encoding='utf-8') as f:
        json.dump(exchange_rates, f, ensure_ascii=False, indent=4)
    
# if __name__ == "__main__":
#     html_content = initialize()
#     get_exchange_rates(html_content)
#     save_to_json()