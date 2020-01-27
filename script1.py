from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html/')
def index():
    return render_template("index.html")

@app.route('/resume.html/')
def resume():
    return render_template("resume.html")

@app.route('/education.html/')
def education():
    return render_template("education.html")

@app.route('/projects.html/')
def projects():
    return render_template("projects.html")

if __name__=="__main__":
    app.run(debug=True)
