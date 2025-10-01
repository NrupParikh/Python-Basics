# python3 -m pip install yfinance
import yfinance as yf
import pandas as pd
import os
import webbrowser
import numpy as np

symbol = "CIPLA.NS"
stock = yf.Ticker(symbol)

print(f"Fetching data for {symbol}")
data = stock.history(period="1y")

# Sort data by date in descending order
data = data.sort_index(ascending=False)

print("Display 1 month data (Latest first)")
print(data.head(30))

# =============== Trend Analysis ===============
# Calculate 50-day and 200-day moving averages
data = data.sort_index(ascending=True)
data["50MA"] = data["Close"].rolling(window=50).mean()
data["200MA"] = data["Close"].rolling(window=200).mean()

# Determine trend based on moving averages
if data["50MA"].iloc[-1] > data["200MA"].iloc[-1]:
    trend = "UPTREND (bullish for next 1-3 months)"
elif data["50MA"].iloc[-1] < data["200MA"].iloc[-1]:
    trend = "DOWNTREND (bearish for next 1-3 months)"
else:
    trend = "SIDEWAYS (uncertain)"

print(f"Trend for {symbol}: {trend}")
# ============================================

data.to_csv("stock_data.csv")
print("Data saved...")

# Convert DataFrame to HTML table and open in browser
data_html = data.reset_index().to_html(index=True)

html_file = "stock_data.html"

# === For better looking HTML file with Bootstrap CSS

html_template = f"""
<html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
          <style>
            th {{
                text-align: center;
            }}
            td {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Last month Stock Data of {symbol}</h2>
            <h4>Trend: {trend}</h4>            
            {data.reset_index().to_html(classes="table table-striped table-bordered", index=False)}
        </div>
    </body>
</html>
"""

with open(html_file, "w") as f:
    f.write(html_template)

webbrowser.open(f"file://{os.path.abspath(html_file)}")
