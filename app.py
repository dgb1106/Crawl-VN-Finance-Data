from flask import Flask, jsonify, send_file
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

@app.route('/exchange-rates/update', methods=['GET'])
def update_exchange_rates():
    try:
        exchange_rates = ExchangeRates.get_new_exchange_rates()
        return send_file("exchange_rates.json", mimetype="application/json")
    except Exception as e:
        return jsonify({"error": "Failed to update exchange rates", "details": str(e)}), 500

@app.route('/exchange-rates', methods=['GET'])
def exchange_rates():
    try:
        return send_file("exchange_rates.json", mimetype="application/json")
    except Exception as e:
        return jsonify({"error": "Failed to read exchange rates file", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)