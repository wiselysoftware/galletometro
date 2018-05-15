from app import db, app
from flask import render_template, jsonify, request, redirect, url_for, flash
from sqlalchemy import desc
from app.models import *
from datetime import datetime
from app.forms import ContactForm


# Normalizacion y escalamiento de los datos
def galleta_transform(raw_data):
    return int(abs((250 * int(raw_data))/130000))


def te_transorm(raw_data):
    return int(abs((int(raw_data) - 1681.3333)/70480.1))


def cafe_transform(raw_data):
    return int(abs((int(raw_data) + 26199.266)/67009.2))


@app.before_first_request
def create_all():
    db.drop_all()
    db.create_all()


@app.route('/')
def main():
    form = ContactForm()
    return render_template('index.html', form=form)


@app.route('/api/datos', methods=['GET', 'POST'])
def data_points():
    if request.method == 'POST':
        data_gw = request.get_json()
        if data_gw:
            datapoints = data_gw['data'].rstrip().split(',')
            new_data_point = DataPoint(
                date=datetime.utcnow(),
                cafe_punto=cafe_transform(datapoints[0]),
                te_punto=te_transorm(datapoints[1]),
                g1_punto=galleta_transform(datapoints[2]),
                g2_punto=galleta_transform(datapoints[3])
            )
            db.session.add(new_data_point)
            db.session.commit()
            return "OK"
    last_data_point = DataPoint.query.order_by(desc(DataPoint.date)).first()
    if last_data_point:
        return jsonify(last_data_point.return_list_data)
    else:
        return "sin datos aun"


@app.route('/api/contact', methods=['GET','POST'])
def contact_info():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_contact = Contact(
                name= form.name.data,
                email = form.email.data,
                message = form.message.data
            )
            db.session.add(new_contact)
            db.session.commit()
            flash("Mensaje enviado!")
            return redirect(url_for('main'))
        else:
            for error in form.errors:
                flash(form.errors[error][0])
            return redirect(url_for('main'))
    else:
        return "WAT"
