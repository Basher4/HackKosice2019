from flask import Flask, jsonify, request
import patient
import doctor
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/patient/enqueue")
def patient_enqueue():
    data = request.get_json()
    return patient.enqueue(data)

@app.route("/api/patient/cancel")
def patient_cancel():
    data = request.get_json()
    return patient.cancel(data)

@app.route("/api/doctor/appointment")
def doctor_appointment():
    data = request.get_json()
    return doctor.new_appointment(data)

@app.route("/api/doctor/entered")
def doctor_entered():
    data = request.get_json()
    return doctor.new_appointment(data)

@app.route("/api/stats")
def stats():
    return jsonify({"response":"idk"})
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)