#python -m venv venv
#venv/Scripts/activate
from flask import Flask, render_template
import requests

app = Flask(__name__)
API = "a8kOsV3sjFAcwZlLbLhBnguspOa4fcTnyPE9iv39"
URL = "https://api.nasa.gov/insight_weather/"

@app.route("/", methods=["GET"])
def index():
    params = {
        "api_key": API,
        "feedtype": "json",
        "ver": "1.0"
    }
    response = requests.get(URL, params=params)
    wather = response.json()

    return render_template("index.html", weather=wather)

if __name__ == "__main__":
    app.run(debug=True)
