import yfinance as yf
import pandas as pd
import numpy as np
import os
import webbrowser
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# =============== Data Fetching ===============
def fetch_stock_data(symbol, period="5y"):
    """Fetch historical stock data from Yahoo Finance"""
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    data = data.sort_index(ascending=True)
    return data


# =============== Technical Indicators ===============
def calculate_moving_averages(data):
    data["50MA"] = data["Close"].rolling(window=50).mean()
    data["200MA"] = data["Close"].rolling(window=200).mean()
    return data


def determin_trend(data):
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
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))
    return data


def calculate_MACD(data, fast=12, slow=26, signal=9):
    data["EMA_fast"] = data["Close"].ewm(span=fast, adjust=False).mean()
    data["EMA_slow"] = data["Close"].ewm(span=slow, adjust=False).mean()
    data["MACD"] = data["EMA_fast"] - data["EMA_slow"]
    data["MACD_signal"] = data["MACD"].ewm(span=signal, adjust=False).mean()
    return data


# =============== Random Forest Forecast ===============
"""
This function uses a Random Forest ML model to learn from
historical stock indicators and predict stock prices for the next 30 days.
"""


def random_forest_forecast(data, days_ahead=30):
    """
    Predict future stock prices using Random Forest Regressor
    """
    df = data.copy()
    # next-day close as target
    df["Target"] = df["Close"].shift(-1)
    df = df.dropna()

    # Features (you can add more indicators here)
    features = ["Close", "50MA", "200MA", "RSI", "MACD", "MACD_signal"]
    df = df.dropna()  # drop rows with NaN from indicators
    X = df[features]
    y = df["Target"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Train model
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Random Forest MAE: {mae:.2f}")

    # Forecast future price iteratively
    last_known = X.iloc[-1].values.reshape(1, -1)
    forecast_prices = []
    for _ in range(days_ahead):
        pred = model.predict(last_known)[0]
        forecast_prices.append(pred)
        # update only Close for simplicity
        last_known[0, 0] = pred

    return forecast_prices[-1], forecast_prices


# =============== Entry / Stoploss ===============
def calculate_entry_stoploss(data, trend, stoploss_percent=5):
    entry_price = None
    stop_loss = None
    if (
        trend.startswith("UPTREND")
        and data["RSI"].iloc[-1] < 70
        and data["MACD"].iloc[-1] > data["MACD_signal"].iloc[-1]
    ):
        entry_price = data["Close"].iloc[-1]
        stop_loss = entry_price * (1 - stoploss_percent / 100)
    return entry_price, stop_loss


# =============== HTML Report Generation ===============
def generate_html_report(
    data,
    symbol,
    trend,
    predicted_price,
    entry_price=None,
    stop_loss=None,
    price_difference=None,
    profit_or_loss=None,
):
    html_file = f"{symbol}_stock_data.html"
    current_price = data["Close"].iloc[-1]
    last_date = data.index[-1].date()
    future_date = datetime.now().date() + timedelta(days=30)

    entry_info = (
        f"Recommended Entry Price: {entry_price:.2f}"
        if entry_price
        else "No Entry Signal"
    )
    stop_info = f"Stop-Loss Level: {stop_loss:.2f}" if stop_loss else ""

    table_html = data.reset_index().to_html(
        classes="table table-striped table-bordered", index=False
    )

    html_template = f"""
    <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
            <style>th, td {{text-align:center}} p{{margin:2px 0}}</style>
        </head>
        <body>
            <div class="container my-3">
                <h4>Last 30 Days Stock Data of {symbol}</h4>
                <p><strong>Trend:</strong> {trend}</p>
                <p><strong>Current Price:</strong> {current_price:.2f} on {last_date}</p>
                <p><strong>Predicted Price (1 month):</strong> {predicted_price:.2f} on {future_date}</p>
                <p><strong>Price Difference:</strong> {price_difference if price_difference else '-'}</p>
                <p><strong>Profit or Loss:</strong> {profit_or_loss if profit_or_loss else '-'}</p>
                <p>{entry_info}</p>
                <p>{stop_info}</p>
                {table_html}
            </div>
        </body>
    </html>
    """
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    webbrowser.open(f"file://{os.path.abspath(html_file)}")


# =============== Main Execution ===============
if __name__ == "__main__":
    symbol = "TATAMOTORS.NS"  # Ola Electric stock symbol on NSE
    data = fetch_stock_data(symbol, period="5y")
    data = calculate_moving_averages(data)
    trend = determin_trend(data)
    data = calculate_RSI(data)
    data = calculate_MACD(data)

    # Random Forest Forecast
    predicted_price, forecast_prices = random_forest_forecast(data, days_ahead=30)

    # Entry & Stoploss
    entry_price, stop_loss = calculate_entry_stoploss(data, trend)

    data.to_csv(f"{symbol}_stock_data.csv")
    last_30_days_data = data.tail(30)
    current_price = data["Close"].iloc[-1]
    price_difference = f"{predicted_price - current_price:.2f}"
    profit_or_loss = f"{((predicted_price - current_price)/current_price)*100:.2f}%"

    # Generate HTML report
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
