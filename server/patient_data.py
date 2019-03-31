
def PatientFromJson(data):
    return PatientData(data["id"],
                       data["email"],
                       data["typ"],
                       data["appointment_time"],
                       data["travel_time"])

def PatientFromJson1(data):
    return PatientFromJson(data)

class PatientData():
    patient_number = 1

    def __init__(self, id, email, msg_type, appointment_time, travel_time):
        self.id = id
        self.email = email
        self.type = msg_type
        self.appointment_time = int(appointment_time)
        self.email_timer = None
        self.sn = PatientData.patient_number
        PatientData.patient_number += 1

        try:
            self.travel_time = int(travel_time)
        except:
            self.travel_time = travel_time
