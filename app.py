from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model= joblib.load("Gradient_boost")
        pred = model.predict([[income, age, loan]])
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="Please input required values"))

if __name__ == "__main__":
    app.run()

