import matplotlib.pyplot as plt
import base64
from io import BytesIO

def plot_stock_data(data, ticker):  # Accept `ticker` as a second argument
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], color="blue")
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title(f"Stock Price for {ticker}")  # Use ticker in the title
        plt.grid(True)

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()
        print("Generated plot URL")  # Debug print
        return plot_url
    except Exception as e:
        print(f"Error generating plot: {e}")
        return None
