import os
import json
from flask import Flask, render_template, request, flash
# Flashed messages stay on screen until refreshed.
# After entering data into contact form to show success.
# Create SECRET_KEY
if os.path.exists("env.py"):
    import env


app = Flask(__name__)  # creates instance of class, stores imported classes ^
app.secret_key = os.environ.get("SECRET_KEY")
# add flash message below contact request.method


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


@app.route("/recipes/<recipe_name>")
def recipes_recipe(recipe_name):
    recipe = {}
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                recipe = obj
    return render_template("instructions.html", recipe=recipe)


@app.route("/contact", methods=["GET", "POST"])
# Flask needs to be explicitly told to accept POST method
def contact():
    if request.method == "POST":
        # flashed message
        flash("Your message has been received. Thank you, {}.".format(
          request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/recommend")
def recommend():
    return render_template("recommend.html", page_title="Our Recommendations")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
