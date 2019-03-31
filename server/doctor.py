from flask import jsonify

def new_appointment(hkqueue, data):
    return jsonify({})

def patient_entered(hkqueue, data):
    hkqueue.remove_patient()
    return jsonify({"patients_left": hkqueue.get_patients_in_queue()})