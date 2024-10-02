import json
from flask import Flask, request, jsonify
from fizzbuzz import fizz
from utils import jsonutils
from dataclasses import asdict


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/fizzbuzz", methods = ['POST'])
def fizzbuzz():
    obj = jsonutils.from_json(request.get_data(), fizz.FizzbuzzInput)
    if isinstance(obj, Exception):
        return obj.__str__(), 400
    
    return  jsonify(asdict(fizz.Compute(obj)))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")