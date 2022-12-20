from tasks import sum_int
from flask import Flask, request
from models import CarsModel

app = Flask(__name__)

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





