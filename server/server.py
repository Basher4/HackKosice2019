from flask import Flask, jsonify, request
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/patient/enqueue")
def patient_enqueue():
    data = request.get_json()
    resp = {
        "full": False,
        "pos_in_queue": 25,
        "waiting_time": 25*12
    }

    return jsonify(resp)

@app.route("/api/patient/cancel")
def patient_cancel():
    return ""

@app.route("/api/stats")
def stats():
    return jsonify({"response":"idk"})
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)