import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/projects')
def hello_projects():
    return render_template("projects.html")

@app.route('/blog')
def hello_blog():
    return render_template("blog.html")

if __name__ == '__main__':
    app.run(debug=True)

