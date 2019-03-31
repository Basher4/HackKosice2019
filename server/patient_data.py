from hkqueue import HkQueue

def PatientFromJson(data):
    return PatientData(data["id"],
                       data["email"],
                       data["typ"],
                       data["appointment_time"],
                       data["travel_time"])

def PatientFromJson1(data):
    return PatientFromJson(data)

class PatientData():
    def __init__(self, id, email, msg_type, appointment_time, travel_time):
        self.id = id
        self.email = email
        self.type = msg_type
        self.appointment_time = int(appointment_time)
        self.email_timer = None
        try:
            self.travel_time = int(travel_time)
        except:
            self.travel_time = travel_time
