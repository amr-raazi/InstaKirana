from flask import Flask, request, render_template, session, redirect

import helper

app = Flask(__name__)
app.secret_key = "XYZ"


@app.route("/")
def index():
    helper.init_vars(session)
    return render_template("index.html")


@app.route("/item/<int:id>", methods=["POST", "GET"])
def item(id):
    helper.init_vars(session)
    if request.method == "POST":
        helper.update_qty(session, str(id), request.form.get("qty_add", 0))
    return render_template("item.html", id=id)


@app.route("/cart", methods=["POST", "GET"])
def cart():
    helper.init_vars(session)
    if session["qty_dict"] == {}:
        return render_template("empty cart.html")
    if request.method == "POST":
        if "increment" in request.form:
            helper.update_qty(session, request.form["increment"], +1)
            return redirect(request.url)
        elif "decrement" in request.form:
            helper.update_qty(session, request.form["decrement"], -1)
            return redirect(request.url)
        elif "clear_cart" in request.form:
            helper.make_qty_zero(session)
            return redirect(request.url)
    return render_template("cart.html")


@app.route("/receipt")
def receipt():
    helper.init_vars(session)
    return render_template("receipt.html")


if __name__ == "__main__":
    app.run(debug=True)
