from flask import Flask

app = Flask(__name__)

average_tine_in = 12
start_time = 8 * 60
end_time = 16 * 60
last_avail = start_time
patients_data = {}
timeline = [False for i in range(end_time - start_time)]
available = True


def move(id, last_avail, timeline, patients_data):
    global average_tine_in
    recent_time = False
    if not timeline[last_avail - start_time + average_tine_in]:
        recent_time = move(timeline[last_avail - start_time + average_tine_in], last_avail + average_tine_in, timeline,
                           patients_data)
    for i in range(average_tine_in):
        timeline[last_avail - start_time + 1 + i] = id
    if recent_time:
        return recent_time
    else:
        return last_avail + average_tine_in


@app.route("/")
def hello():
    json = request.get_json()
    return "Hello World!"


if __name__ == "__main__":
    app.run()

patient = {'id': 00,
           'typ': 00,
           'email': 00,
           'q_num': 00,
           'enter_time': last_avail}

patients_data[patient[id]] = patient
last_avail = patient['enter_time'] + average_tine_in
if not timeline[last_avail - start_time]:
    recent_time = move(timeline[last_avail - start_time], last_avail, timeline, patients_data)
for i in range(average_tine_in):
    timeline[last_avail - start_time + 1 + i] = patient['id']

if recent_time >
    if recent_time >= end_time:
        available = False










