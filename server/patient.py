from flask import jsonify
import patient_data

def enqueue(hkqueue, data):
    print(data)
    resp = {
        "full": False,
        "pos_in_queue": data.id,
        "waiting_time": 20
    }

    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})