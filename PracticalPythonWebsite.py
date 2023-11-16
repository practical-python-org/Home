"""
This is a comment from Xarlos!
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', '[POST'])
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/FAQ")
def faq():
    return render_template("faq.html")

@app.route("/features")
def features():
    return render_template("features.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# Websites URL: http://127.0.0.1:8080