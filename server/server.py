from flask import Flask, jsonify, request, render_template
import patient, doctor, hkqueue, stats
import patient_data as pd
import json
app = Flask(__name__)

@app.before_first_request
def initialize():
    app.config["hkqueue"] = hkqueue.HkQueue()

@app.route("/")
def root():
    return render_template("index.html", users=len(app.config['hkqueue'].timeline))

@app.route("/dbg")
def hello():
    hkqueue = app.config["hkqueue"]
    output = "Queue Length: " + str(len(hkqueue.timeline)) + "<br>"
    for p in hkqueue.timeline:
        output += "[{}] @ {} - {}<br/>".format(p.sn, p.appointment_time, p.appointment_time + hkqueue.avg_examination_time)
    return output

@app.route("/api/patient/enqueue", methods = ["POST"])
def patient_enqueue():
    data = json.loads(request.data.decode("utf-8"))
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

@app.route("/api/doctor/entered", methods = ["GET"])
def doctor_entered():
    return doctor.patient_entered(app.config["hkqueue"])

@app.route("/api/stats/status", methods = ["POST", "GET"])
def stats_status():
    return stats.now_waiting(app.config["hkqueue"])
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)