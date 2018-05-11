from app import db, app
from flask import render_template
from app.models import *

@app.before_first_request
def create_all():
    db.drop_all()
    db.create_all()


@app.route('/')
def main():
    return "sup"


@app.route('/api/data', methods=['GET', 'POST'])
def data_points():
    if request.method == 'POST':
        print(r.json)
        return "OK"
    else:
        return render_template('index.html')
