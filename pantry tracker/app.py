from flask import Flask, render_template, redirect, url_for, request
from pantry import Item, Pantry

app = Flask(__name__)
p = Pantry()

@app.route("/")
def index():
    print(p.table)
    return render_template("index.html", pantry=p)

@app.route("/add", methods=["POST"])
def form_add():
    p.add(Item(request.form["name"], request.form["category"]))
    return redirect(url_for("index"))

@app.route("/add/<name>/<type>", methods=["POST"])
def add(name, type):
    p.add(Item(name, type))
    return redirect(url_for("index"))

@app.route("/delete/<name>/<type>", methods=["POST"])
def delete(name, type):
    p.remove(Item(name, type))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
