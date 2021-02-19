import os
import json
from flask import Flask, render_template


app = Flask(__name__)  # creates instance of class, stores imported classes ^


@app.route("/")  # all functions are objects so can be passed around @
def index():
    return render_template("index.html", )


@app.route("/recipes")
def recipes():
  data = []
  with open("data/recipes.json", "r") as json_data:
    data = json.load(json_data)
    return render_template(
      "recipes.html", page_title="All Recipes", recipes=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/recommend")
def recommend():
    return render_template("recommend.html", page_title="Our Recommendations")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
