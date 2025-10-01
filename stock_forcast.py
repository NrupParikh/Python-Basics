import yfinance as yf
import pandas as pd
import os
import webbrowser
import numpy as np
from datetime import datetime


def fetch_stock_data(symbol, period):
    """Fetch historical data from Yahoo Finance"""
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    data = data.sort_index(ascending=True)
    return data


def calculate_moving_averages(data):
    """Calculate 50-day and 200-day moving averages"""
    data["50MA"] = data["Close"].rolling(window=50).mean()
    data["200MA"] = data["Close"].rolling(window=200).mean()
    return data


def determin_trend(data):
    """Determine trend based on moving averages"""
    if (
        data["50MA"].iloc[-1] > data["200MA"].iloc[-1]
        and data["Close"].iloc[-1] > data["50MA"].iloc[-1]
    ):
        trend = "UPTREND (bullish for next 1-3 months)"
    elif (
        data["50MA"].iloc[-1] < data["200MA"].iloc[-1]
        and data["Close"].iloc[-1] < data["50MA"].iloc[-1]
    ):
        trend = "DOWNTREND (bearish for next 1-3 months)"
    else:
        trend = "SIDEWAYS (uncertain)"
    return trend


def calculate_RSI(data, window=14):
    """Calculate Relative Strength Index (RSI)"""
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))
    return data


def calculate_MACD(data, fast=12, slow=26, signal=9):
    """Calculate MACD with customizable spans"""
    data["EMA_fast"] = data["Close"].ewm(span=fast, adjust=False).mean()
    data["EMA_slow"] = data["Close"].ewm(span=slow, adjust=False).mean()
    data["MACD"] = data["EMA_fast"] - data["EMA_slow"]
    data["MACD_signal"] = data["MACD"].ewm(span=signal, adjust=False).mean()
    return data


def monte_carlo_forecast(data, days=30, simulations=1000):
    """Perform Monte Carlo Simulation for Stock price prediction"""
    data["Return"] = data["Close"].pct_change()
    data.dropna(inplace=True)
    last_price = data["Close"].iloc[-1]
    mu = data["Return"].mean()
    sigma = data["Return"].std()

    simulated_prices = np.zeros((days, simulations))
    for i in range(simulations):
        price = last_price
        for d in range(days):
            price *= 1 + np.random.normal(mu, sigma)
            simulated_prices[d, i] = price

    expected_prices = simulated_prices[-1].mean()
    return expected_prices, simulated_prices


def calculate_entry_stoploss(data, trend, stoploss_percent=5):
    """Determine entry and stoploss based on trend,RSI and MACD"""
    entry_price = None
    stop_loss = None

    if (
        trend.startswith("Strong UPTREND")
        and data["RSI"].iloc[-1] < 70
        and data["MACD"].iloc[-1] > data["MACD_signal"].iloc[-1]
    ):
        entry_price = data["Close"].iloc[-1]
        stop_loss = entry_price * (1 - stoploss_percent / 100)

    return entry_price, stop_loss


# =============== HTML Report Generation ===============


def generate_html_report(
    data: pd.DataFrame,
    symbol: str,
    trend: str,
    predicted_price: float,
    entry_price: float = None,
    stop_loss: float = None,
    price_difference: float = None,
    profit_or_loss: float = None,
):
    """Generate an HTML stock report with Bootstrap styling."""

    # File name
    html_file = f"{symbol}_stock_data.html"

    # Prepare dynamic fields
    current_price = data["Close"].iloc[-1]
    last_date = data.index[-1].date()
    future_date = datetime.now().date() + pd.Timedelta(days=30)

    entry_info = (
        f"Recommended Entry Price: {entry_price:.2f}"
        if entry_price is not None
        else "No Entry Signal"
    )
    stop_info = f"Stop-Loss Level: {stop_loss:.2f}" if stop_loss is not None else ""

    # Convert table to HTML
    table_html = data.reset_index().to_html(
        classes="table table-striped table-bordered", index=False
    )

    # Build HTML
    html_template = f"""
    <html>
        <head>
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
            <style>
                th, td {{ text-align: center; }}
                p {{ margin: 2px 0; }}
                 .no-margin-container {{
                    margin-left: 10 !important;
                    margin-right: 0 !important;
                    padding-left: 5px;
                    padding-right: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="container-fluid no-margin-container my-3">
                <h4 class="mb-3">Last 30 Days Stock Data of {symbol}</h4>                
                <p><strong>Trend:</strong> {trend}</p>
                <p><strong>Current Price:</strong> {current_price:.2f} on {last_date}</p>
                <p><strong>Predicted Price (1 month):</strong> {predicted_price:.2f} on {future_date}</p>
                <p><strong>Price Difference:</strong> {price_difference if price_difference is not None else '-'}</p>
                <p><strong>Profit or Loss:</strong> {profit_or_loss if profit_or_loss is not None else '-'}</p>
                <p>{entry_info}</p>
                <p>{stop_info}</p>            
                {table_html}
            </div>
        </body>
    </html>
    """

    # Write file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_template)

    # Open in browser
    webbrowser.open(f"file://{os.path.abspath(html_file)}")


# =============== Main Execution ===============
symbol = "TATAMOTORS.NS"
# Fetch 1 year data
data = fetch_stock_data(symbol, period="1y")
# Calculate moving averages and trend
data = calculate_moving_averages(data)
trend = determin_trend(data)

# Technical Indicators
data = calculate_RSI(data)
data = calculate_MACD(data)

# Monte Carlo Forecast
predicted_price, simulations = monte_carlo_forecast(data)

# Entry and Stoploss
entry_price, stop_loss = calculate_entry_stoploss(data, trend)

data.to_csv(f"{symbol}_stock_data.csv")

# Display last 30 days data
last_30_days_data = data.tail(30)
print(last_30_days_data)

# Get closing price of the last day
current_price = data["Close"].iloc[-1]
current_date = data.index[-1].date()
price_difference = f"{predicted_price - current_price:.2f}"
profit_or_loss = f"{((predicted_price - current_price) / current_price) * 100:.2f}%"

# Generate HTML Report
generate_html_report(
    last_30_days_data,
    symbol,
    trend,
    predicted_price,
    entry_price,
    stop_loss,
    price_difference,
    profit_or_loss,
)
