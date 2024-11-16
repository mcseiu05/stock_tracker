import matplotlib.pyplot as plt
import base64
from io import BytesIO

def plot_stock_data(data, ticker):
    """
    Generate a base64-encoded plot for the given stock data and ticker symbol.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label=f"{ticker} Price", color="blue")
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title(f"{ticker} Stock Price")
        plt.grid(True)
        plt.legend()

        # Save the plot to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Encode the image as base64
        plot_url = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()  # Close the plot to free memory
        return plot_url
    except Exception as e:
        print(f"Error generating plot: {e}")
        return None
