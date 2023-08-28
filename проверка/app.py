from flask import Flask, render_template, request
import db

db.clear_db()
db.create()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/math_test.html')
def math1():
    return render_template("math_test.html")

@app.route('/math_test2.html', methods=['GET', 'POST'])
def math2():
    result = request.form.get("answer1_m")
    return render_template("math_test2.html", result=result)

@app.route('/math_test3.html', methods=['GET', 'POST'])
def math3():
    result = request.form.get("answer2_m")
    return render_template("math_test3.html", result=result)

@app.route('/math_test4.html', methods=['GET', 'POST'])
def save_name():
    result = request.form.get("answer3_m")
    if request.method == "POST":
        name = request.form.get("name")
        db.insert_db(name)
    return render_template("math_test4.html", result=result)

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run()