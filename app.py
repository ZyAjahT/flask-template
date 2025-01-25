from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/album")
def album():
    return render_template("album.html")


if __name__ == "main":
    app.run(debug=True)