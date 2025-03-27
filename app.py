from flask import Flask, jsonify
import WebScraping
import ExchangeRates
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/indices', methods=['GET'])
def indices():
    return jsonify(WebScraping.getIndices())

@app.route('/commodities', methods=['GET'])
def commodities():
    return jsonify(WebScraping.getCommodities())

@app.route('/cryptos', methods=['GET'])
def cryptos():
    return jsonify(WebScraping.getCryptos())

@app.route('/exchange-rates', methods=['GET'])
def exchange_rates():
    return jsonify(ExchangeRates.get_current_exchange_rates())

@app.route('/update-exchange-rates', methods=['GET'])
def update_exchange_rates():
    return jsonify(ExchangeRates.get_new_exchange_rates())

if __name__ == '__main__':
    app.run(debug=True)