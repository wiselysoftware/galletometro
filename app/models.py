from app import db


class DataPoint(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    cafe_punto = db.Column(db.Integer())
    te_punto = db.Column(db.Integer())
    g1_punto = db.Column(db.Integer())
    g2_punto = db.Column(db.Integer())

    @property
    def return_list_data(self):
        return [
            self.date.isoformat(),
            self.cafe_punto,
            self.te_punto,
            self.g1_punto,
            self.g2_punto
        ]
    

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(24))
    message = db.Column(db.Text())
