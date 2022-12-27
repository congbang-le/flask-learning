from turtle import update
from tasks import sum_int
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())   # Fortuner
    brand = db.Column(db.String())  # Toyota
    type = db.Column(db.String())   # SUV
    seats = db.Column(db.Integer)   # 4

    def __init__(self, name, brand, type, seats):
        self.name = name
        self.brand = brand
        self.type = type
        self.seats = seats

    def __repr__(self):
        return f"<Car {self.name}>"
    
    def serialize(self):
        return {"id": self.id,
                "name": self.name}


@app.get("/health")
def healthcheck():
    return "Healthy", 200

@app.post("/sum")
def run_task():
    try:
        data = request.json
        task = sum_int.delay(data["first_int"] , data["second_int"])
        return f"success with {task}", 201
    except:
        return "Failed", 404

@app.post('/cars')
def create_car():
    if request.is_json:
        data = request.json
        new_car = CarsModel(name=data['name'], brand=data['brand'], type=data['type'], seats=data['seats'])
        db.session.add(new_car)
        db.session.commit()
        return {"message": f"car {new_car.name} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}, 404

@app.get('/cars')
def get_all():
    cars = CarsModel.query.all()
    results = [
        {
            "name": car.name,
            "brand": car.brand,
            "type": car.type,
            "seats": car.seats,
        } for car in cars]

    return {"count": len(results), "cars": results}

@app.get('/cars/<int:id>')
def get_car(id):
    return jsonify({'car': CarsModel.query.get(id).serialize()})

@app.put('/cars/<int:id>')
def update_car(id):
    updated_car = CarsModel.query.get(id)
    updated_car.name = request.json.get('name', updated_car.name)
    db.session.commit()
    return jsonify({'car': updated_car.serialize()})

@app.delete('/cars/<int:id>')
def delete_car(id):
    db.session.delete(CarsModel.query.get(id))
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)




