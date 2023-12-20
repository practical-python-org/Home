from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route("/FAQ", methods=['GET'])
def faq():
    return render_template("faq.html")

@app.route("/features", methods=['GET'])
def features():
    return render_template("features.html")



