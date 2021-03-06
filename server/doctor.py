from flask import jsonify
from datetime import datetime


def new_appointment(hkqueue, data):
    hkqueue.add_patient(data)
    return jsonify({})


def patient_entered(hkqueue):
    if len(hkqueue.timeline) == 0:
        return jsonify()
    pat_now = hkqueue.timeline.pop(0)
    hkqueue.end_index -= 1
    if len(hkqueue.timeline) > 0:
        time_ap = hkqueue.timeline[0].appointment_time
        time_now = datetime.now().hour * 60 + datetime.now().minute
        change = (time_now + hkqueue.avg_examination_time) - time_ap
        for i in range(hkqueue.end_index):
            print(hkqueue.end_index)
            hkqueue.timeline[i].offset_appointment(change) # reschedules email
    new_pat_now = {
            "id": pat_now.id,
            "email": pat_now.email,
            "typ": pat_now.type,
            "appointment_time": pat_now.appointment_time,
            "travel_time": pat_now.travel_time}
    return jsonify(new_pat_now)
