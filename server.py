from flask import Flask, render_template, request, redirect
from uuid import uuid1

app = Flask(__name__)
ids = [str(uuid1()).split("-")[0] for x in range(10)]


@app.route("/")
def index():
    return render_template("index.html", ids=ids)


@app.route("/vote/")
def vote():
    print("\n\nSe petrec chestii\n\n")
    id = request.values.get("id")
    return redirect(f"/#{id}")


if __name__ == "__main__":
    app.run(debug=True)
