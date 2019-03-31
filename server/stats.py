from flask import jsonify
from datetime import datetime

def now_waiting(hkqueue):
    resp = {
        "waiting": hkqueue.get_patients_in_queue(),
        "full": hkqueue.get_patients_in_queue()*hkqueue.avg_examination_time >= (hkqueue.end_time - (datetime.now().hour * 60 + datetime.now().minute))/hkqueue.avg_examination_time,
        "pos_in_queue": hkqueue.get_patients_in_queue()
    }

    return jsonify(resp)