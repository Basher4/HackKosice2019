from flask import jsonify
import patient_data
import datetime

def enqueue(hkqueue, data):
    if (len(hkqueue.timeline) == 0) or (hkqueue.timeline[hkqueue.end_index].appointment_time > hkqueue.avg_examination_time + 10 + int(datetime.datetime.now()[15:17])*60 + int(datetime.datetime.now()[18:20])):
        if (int(datetime.datetime.now()[15:17])*60 + int(datetime.datetime.now()[18:20])) < hkqueue.start_time:
            data.appointment_time = hkqueue.start_time
        else:
            data.appointment_time = int(datetime.datetime.now()[15:17])*60 + int(datetime.datetime.now()[18:20])
    else:
        data.appointment_time = hkqueue.timeline[hkqueue.end_index].appointment_time
    stav = hkqueue.get_first_free_slot()
    resp = {
        "full": stav,
        "pos_in_queue": str(len(hkqueue.timeline)),
        "waiting_time": str(len(hkqueue.timeline))*hkqueue.avg_examination_time
    }
    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})