from hkqueue import HkQueue

def PatientFromJson(data, appointment_time):
    return PatientData(data["id"],
                       data["email"],
                       appointment_time,
                       data["travel_time"])

def PatientFromJson1(data):
    return PatientFromJson(data, -1)

class PatientData():
    def __init__(self, id, email, appointment_time, travel_time):
        self.id = id
        self.email = email
        self.travel_time = travel_time
        self.appointment_time = appointment_time
