import time
import threading
import yfinance as yf
from flask import Flask, render_template
from flask_socketio import SocketIO
from utils import plot_stock_data  # Assuming utils.py exists

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def fetch_stock_data(ticker):
    """Fetch stock data for the given ticker symbol."""
    try:
        stock = yf.Ticker(ticker)
        return stock.history(interval="1m", period="1d")
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def stock_price_monitor(ticker):
    """Continuously monitor stock price and emit updates."""
    while True:
        data = fetch_stock_data(ticker)
        if data is not None and not data.empty:
            latest_price = data['Close'].iloc[-1]
            plot_url = plot_stock_data(data, ticker)

            if plot_url:
                socketio.emit('update_price', {'price': round(latest_price, 2)})
                socketio.emit('update_chart', {'plot_url': plot_url})

        time.sleep(60)

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

@socketio.on('get_data')
def on_get_data(ticker):
    """Start monitoring stock data for the given ticker."""
    print(f"Starting monitoring for: {ticker}")
    threading.Thread(target=stock_price_monitor, args=(ticker,), daemon=True).start()

@app.route('/')
def home():
    """Render the main application page."""
    return render_template('app.html')

if __name__ == '__main__':
    socketio.run(app)
