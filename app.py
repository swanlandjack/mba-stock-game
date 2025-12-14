from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yfinance as yf
import os

# Initialize Flask
# We tell it to look for HTML files in the 'templates' folder
app = Flask(__name__, template_folder='templates')
CORS(app)

# --- ROUTE 1: THE WEBSITE (Frontend) ---
@app.route('/')
def home():
    # This serves your game.html file to the browser
    return render_template('game.html')

# --- ROUTE 2: THE API (Backend Logic) ---
def analyze_stock(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="5d")
        if hist.empty: return None
        current = hist['Close'].iloc[-1]
        prev = hist['Close'].iloc[-2]
        change_pct = ((current - prev) / prev) * 100
        direction = "UP" if change_pct > 0 else "DOWN"
        return {
            "current": round(current, 2),
            "prev": round(prev, 2),
            "percent": round(change_pct, 2),
            "direction": direction
        }
    except: return None

@app.route('/guess', methods=['GET'])
def judge_guess():
    ticker = request.args.get('ticker', 'AAPL').upper()
    prediction = request.args.get('prediction', 'UP').upper()
    data = analyze_stock(ticker)
    
    if not data:
        return jsonify({"error": "Stock not found"}), 404
    
    result = "WIN" if prediction == data['direction'] else "LOSS"
    
    return jsonify({
        "result": result,
        "details": f"{ticker} moved {data['direction']} by {data['percent']}%"
    })

if __name__ == '__main__':
    # Cloud servers use a specific port defined in the environment
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)