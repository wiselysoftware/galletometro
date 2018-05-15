from app import db


class DataPoint(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    graph_name = db.Column(db.String(24)) 
    point_date = db.Column(db.DateTime())
    

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(24))
    message = db.Column(db.Text())
