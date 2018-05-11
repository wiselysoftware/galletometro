from app import db

class DataPoing(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    graph_name = db.Column(db.String(24)) 
    point_date = db.Column(db.DateTime())
    
