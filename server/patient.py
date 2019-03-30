from flask import jsonify
import patient_data

def enqueue(hkqueue, data):
    resp = {
        "full": False,
        "pos_in_queue": hkqueue.other_time,
        "waiting_time": hkqueue.average_time_sth
    }

    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})