from flask import Flask, request
from fizzbuzz import Compute, FizzbuzzInput
from utils import from_json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/fizzbuzz", methods = ['POST'])
def fizzbuzz():
    obj = from_json(request.get_json())
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")