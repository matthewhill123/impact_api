from flask import Flask, Response, request, jsonify
from convert_co2 import convert_to_co2
from compute_warming import compute_warming_from_co2

app = Flask(__name__)
app.secret_key = b"%$\xf9\xbd\xb1\xf3\x17,\x81]\x1f\xd7\xc3v\x03\xe57&q\x9e\x99F\x19\xa1"


@app.route('/transport', methods=["POST"])
def get_warming_from_transport():

    events = request.json
    print(events)
    value_co2 = convert_to_co2(events)

    warming = compute_warming_from_co2(value_co2)

    return jsonify(events)
