from flask import Flask, render_template
import requests
import logging
app = Flask(__name__)

@app.route("/")
def home():
    try:
        URL = "https://xkcd.com/info.0.json"
        response = requests.get(url = URL)
        if(response.status_code != 200):
            raise ValueError(f"Error connecting to XKCD please check back later.")
        return render_template("index.html", data = response.json()) 
    except ValueError as e:
        logging.error(f"ValueError with home: {e}")
        return render_template("errorPage.html", errorMessage = e)

@app.route("/pastComic/<comicNum>")
def pastComic(comicNum):
    try: 
        logging.info(f"Past Comic URL with value : {comicNum}")
        if not comicNum.isdigit():
            raise ValueError(f"The requested comic should be a integer. Received '{comicNum}' instead")
        if(int(comicNum) > 3000):
            raise ValueError(f"No comics available for '{comicNum}', Please try another number smaller than 3001")
        URL = "https://xkcd.com/" + comicNum + "/info.0.json"
        response = requests.get(url = URL)
        if(response.status_code != 200):
            raise ValueError(f"Error connecting to XKCD please check back later.")
        return render_template("pastComic.html", data = response.json()) 
    except ValueError as e:
        logging.error(f"ValueError with pastComic: {e}")
        return render_template("errorPage.html", errorMessage = e)
    except Exception as e:  
        logging.error(f"Exception with pastComic: {e}")
        return render_template("errorPage.html", errorMessage = e)

@app.route("/album")
def album():
    return render_template("album.html")

if __name__ == "__main__":
    app.run(debug=True)