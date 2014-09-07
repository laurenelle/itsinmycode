import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_home():
    return render_template("home.html")

@app.route('/about')
def hello_about():
    return render_template("about.html")

@app.route('/contact')
def hello_blog():
    return render_template("contact.html")

@app.route('/projects')
def hello_projects():
    return render_template("projects.html")

if __name__ == '__main__':
    app.run(debug=True)

