import requests
from dotenv import load_dotenv
import os

load_dotenv()

indices = []
commodities = []
cryptos = []

url = os.getenv('URL')

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "client-type": "web",
    "origin": os.getenv('ORIGIN'),
    "referer": os.getenv('REFERER'),
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "timestamp": "1742960869323",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

def getIndices():
    getData()
    return indices

def getCommodities():
    getData()
    return commodities

def getCryptos():
    getData()
    return cryptos

def getData():
    response = requests.get(url, headers=headers)
    json_data = response.json()
    
    indices.clear()
    commodities.clear()
    cryptos.clear()

    for symbol in json_data["data"]["symbols"]:
        symbol_data = symbol.get("data", {})
        code = symbol_data.get("code", "N/A")
        name = symbol_data.get("name", "N/A")
        price = symbol_data.get("price", "N/A")
        day_change = symbol_data.get("dayChange", 0)
        day_change_pct = round(symbol_data.get("dayChangePercent", 0) * 100) / 100
        
        if code in ['VNIndex', 'HNXIndex', 'HNXUpcomIndex', 'VN30', 'US30', 'SP500', 'COMP', 'UK100', 'JPN225', 'HKG33']:
            indices.append(
                {
                    "code": code,
                    "name": name,
                    "price": price,
                    "day_change": day_change,
                    "day_change_pct": day_change_pct
                }
            )
        elif code in ['XAUUSD', 'XAGUSD']:
            commodities.append(
                {
                    "code": code,
                    "name": name,
                    "price": price,
                    "day_change": day_change,
                    "day_change_pct": day_change_pct
                }
            )
        elif code in ['BTCUSDT', 'ETHUSDT']:
            cryptos.append(
                {
                    "code": code,
                    "name": name,
                    "price": price,
                    "day_change": day_change,
                    "day_change_pct": day_change_pct
                }
            )

        # print(f"{code} ({name}): {price} ({day_change:+.2f}, {day_change_pct}%)")