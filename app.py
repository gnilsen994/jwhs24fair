from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "jw2024"

placeholder_names = ["John - 9th Grade", "Jane - 11th Grade", "Alex - 12th Grade", "Emily - 10th Grade", "Chris - 11th Grade"]

@app.route("/hello")
def index():
    flash("Enter your name")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello, " + str(request.form['name_input']))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)