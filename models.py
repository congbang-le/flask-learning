from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    brand = db.Column(db.String())  # Toyota
    type = db.Column(db.String())   # SUV
    seats = db.Column(db.Integer)   # 4
