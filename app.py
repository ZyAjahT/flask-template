from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    URL = "https://xkcd.com/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template("index.html", data = data)

@app.route("/pastComic/<comicNum>")
def pastComic(comicNum):
    if(comicNum.isdigit() and int(comicNum) <= 3000):
        URL = "https://xkcd.com/" + comicNum + "/info.0.json"
        req = requests.get(url = URL)
        data = req.json()
        return render_template("pastComic.html", data = data)   
    else:
        return render_template("errorPage.html")

    
@app.route("/album")
def album():
    return render_template("album.html")

if __name__ == "__main__":
    app.run(debug=True)