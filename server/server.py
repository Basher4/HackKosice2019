from flask import Flask, jsonify, request
import patient, doctor, hkqueue
import patient_data as pd
import json
app = Flask(__name__)

@app.before_first_request
def initialize():
    app.config["hkqueue"] = hkqueue.HkQueue()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/patient/enqueue", methods = ["POST"])
def patient_enqueue():
    data = json.loads(request.data)
    return patient.enqueue(app.config["hkqueue"],
                            pd.PatientFromJson1(data))

@app.route("/api/patient/cancel", methods = ["POST"])
def patient_cancel():
    data = json.loads(request.data)
    return patient.cancel(app.config["hkqueue"],
                            pd.PatientFromJson1(data))

@app.route("/api/doctor/appointment", methods = ["POST"])
def doctor_appointment():
    data = json.loads(request.data)
    return doctor.new_appointment(app.config["hkqueue"],
                                    pd.PatientFromJson1(data))

@app.route("/api/doctor/entered", methods = ["POST"])
def doctor_entered():
    data = json.loads(request.data)
    return doctor.patient_entered(app.config["hkqueue"],
                                    pd.PatientFromJson1(data))

@app.route("/api/stats", methods = ["POST", "GET"])
def stats():
    return jsonify({"response":"idk"})
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)