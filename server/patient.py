from flask import jsonify
import patient_data

def enqueue(hkqueue, data):
    hkqueue.add_patient(data)

    resp = {
        "full": False,
        "pos_in_queue": hkqueue.get_patients_in_queue(),
        "waiting_time": (hkqueue.get_patients_in_queue() - 1) * 12
    }
    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})