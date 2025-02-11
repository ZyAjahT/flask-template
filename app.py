from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/pastComic")
def pastComic():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)   

@app.route("/album")
def album():
    return render_template("album.html")


if __name__ == "__main__":
    app.run(debug=True)