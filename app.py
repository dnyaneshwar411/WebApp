from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        cityName = request.form["cityName"]
        print(cityName)

        payload = {"q": cityName, "appid": "7662f0b8eb37501fdcbd69bee57211db"}
        r = requests.post(
            "https://api.openweathermap.org/data/2.5/weather", params=payload
        )
        y = r.json()
        
        return render_template("WeatherData.html", cityName=cityName, cityWeather=y)


@app.route("/hello")
def hello():
    return "Happy Diwali"


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port="3000")
    app.run()



    
# flask --app example_app.py --debug run