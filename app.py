import time
import threading
import yfinance as yf
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from utils import plot_stock_data  # Assuming utils.py is in the same directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(interval="1m", period="1d")
        print(f"Fetched data for {ticker}: {data.tail()}")  # Debug print
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def background_task(ticker):
    while True:
        data = get_stock_data(ticker)
        if data is not None and not data.empty:
            price = data['Close'].iloc[-1]
            print(f"Latest price for {ticker}: {price}")  # Debug print

            plot_url = plot_stock_data(data, ticker)  # Pass ticker symbol here
            if plot_url:
                socketio.emit('update_price', {'price': round(price, 2)})
                socketio.emit('update_chart', {'plot_url': plot_url})
            else:
                print("Error generating plot URL")  # Debug print

        time.sleep(60)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('get_data')
def handle_get_data(ticker):
    print(f"Starting background task for ticker: {ticker}")  # Debug print
    threading.Thread(target=background_task, args=(ticker,), daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
