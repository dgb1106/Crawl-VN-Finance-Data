from flask import Flask, jsonify
import requests
import WebScraping

app = Flask(__name__)

@app.route('/indices')
def indices():
    return jsonify(WebScraping.getIndices())

@app.route('/commodities')
def commodities():
    return jsonify(WebScraping.getCommodities())

@app.route('/cryptos')
def cryptos():
    return jsonify(WebScraping.getCryptos())

if __name__ == '__main__':
    app.run(debug=True)