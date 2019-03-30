from flask import jsonify

def enqueue(data):
    resp = {
        "full": False,
        "pos_in_queue": 25,
        "waiting_time": 25*12
    }
    return jsonify(resp)

def cancel(data):
    return jsonify({})