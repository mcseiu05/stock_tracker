# Real-Time Stock Price Tracker
## Overview

This Python-based application uses **WebSockets** and the **yfinance** library to track real-time stock prices and display them dynamically in a web browser.

### Features:

- **Real-Time Updates**:  Continuously fetches and displays the latest stock prices.
- **Interactive Visualization**: Utilizes Matplotlib to generate dynamic charts for visual representation of stock price movements.
- **User-Friendly Interface**: Provides a simple web interface to conveniently view the stock data.


## Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/real-time-stock-tracker.git
Use code with caution.

Create a Virtual Environment:

```bash
python -m venv venv
Use code with caution.

Activate the Virtual Environment:

Windows:

```bash
venv\Scripts\activate
Use code with caution.


### Install Dependencies:   

```bash
pip install flask flask-socketio yfinance matplotlib
Use code with caution.

## Usage

### Run the Application:

```bash
python app.py
Use code with caution.

### Access the Web Interface:

Open a web browser and navigate to http://127.0.0.1:5000/ to view the real-time stock price tracker.

## Customization

Ticker Symbols: Modify the ticker variable in the handle_get_data function to track different stocks.
Update Interval: Adjust the time.sleep interval in handle_get_data to control the frequency of price updates.
Visualization: Customize the Matplotlib plots (line styles, colors, etc.) to your preference.
Web Interface: Enhance the index.html template to add features like historical data, technical indicators, or alerts.
Contributing

## We welcome contributions to this project! Feel free to:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes.
- Commit your changes with clear commit messages.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.
