from app import app
from flask import render_template, request, url_for

@app.route('/')
def home():
    name = request.args.get('name')
    number = request.args.get('number')
    if not name:
        name = '<unknow>'
    return render_template('home.jinja', name=name, number=number)
