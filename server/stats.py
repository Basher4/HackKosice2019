from flask import jsonify

def now_waiting(hkqueue):
    resp = {
        "waiting": hkqueue.get_patients_in_queue(),
        "full": hkqueue.get_patients_in_queue() > 5
    }

    return jsonify(resp)