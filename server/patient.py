import email_sender
from flask import jsonify
from datetime import datetime

def enqueue(hkqueue, data):
    hkqueue.add_patient(data)
    if (len(hkqueue.timeline) == 1) or (hkqueue.timeline[hkqueue.end_index].appointment_time > hkqueue.avg_examination_time + 10 + datetime.now().hour * 60 + datetime.now().minute):
        if (datetime.now().hour * 60 + datetime.now().minute) < hkqueue.start_time:
            data.appointment_time = hkqueue.start_time
        else:
            data.appointment_time = datetime.now().hour * 60 + datetime.now().minute
    else:
        data.appointment_time = hkqueue.timeline[hkqueue.end_index].appointment_time
    stav = hkqueue.get_first_free_slot()
    hkqueue.sort_timeline()
    
    resp = {
        "full": stav,
        "pos_in_queue": str(len(hkqueue.timeline)),
        "waiting_time": str((len(hkqueue.timeline)-1)*hkqueue.avg_examination_time)
    }
    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})