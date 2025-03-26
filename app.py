from flask import Flask, jsonify
import requests
import WebScraping

app = Flask(__name__)

@app.route('/indices', methods=['GET'])
def indices():
    return jsonify(WebScraping.getIndices())

@app.route('/commodities', methods=['GET'])
def commodities():
    return jsonify(WebScraping.getCommodities())

@app.route('/cryptos', methods=['GET'])
def cryptos():
    return jsonify(WebScraping.getCryptos())

if __name__ == '__main__':
    app.run(debug=True)