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
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        
        json_data = response.json()
        
        # Clear existing data
        indices.clear()
        commodities.clear()
        cryptos.clear()
        
        # Debug response structure if needed
        # print(json_data.keys())
        
        # Check if 'data' key exists and handle different response structures
        if "data" in json_data and "symbols" in json_data["data"]:
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
        else:
            # Handle case where expected structure isn't present
            print("API response structure has changed")
            print("Available keys:", json_data.keys())
            # Optionally save the response for debugging
            with open('api_response_debug.json', 'w') as f:
                import json as json_lib
                json_lib.dump(json_data, f, indent=2)
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"JSON parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")