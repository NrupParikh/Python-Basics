"""
Micro-framework : Only provides routing, request/response handling
pip3 install flask
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the root URL
@app.route("/")
def home():
    return "Hello, Flask"


# Run the app in debug mode
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)


"""
Run the app: python3 flask_intro.py
Open browser: http://127.0.0.1:5000/
or Run on browser: http://10.37.55.164:5000/
Stop the app: Ctrl + C
"""
