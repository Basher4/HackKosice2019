import email_sender
from flask import jsonify
from datetime import datetime

def enqueue(hq, data):
    minutes_now = datetime.now().hour * 60 + datetime.now().minute
    soonest_time_possible = max(minutes_now + int(data.travel_time), hq.start_time)
    data.appointment_time = soonest_time_possible

    hq.add_patient(data)
    hq.sort_timeline()
    hq.end_index = 0
    stav = hq.fix_timeline_overlaps()

    resp = {
        "full": stav,
        "pos_in_queue": str(hq.timeline.index(data)+1),
        "waiting_time": str((hq.timeline.index(data))*hq.avg_examination_time)
    }
    return jsonify(resp)

def cancel(hkqueue, data):
    return jsonify({})