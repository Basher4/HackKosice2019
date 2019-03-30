def PatientFromJson(data, appointment_time):
    return PatientData(data["id"], data["email"], appointment_time)

class PatientData():
    def __init__(self, id, email, appointment_time):
        self.id = id
        self.email = email
        self.appointment_time = appointment_time

    def offset_appointment(self, deltaT):
        self.appointment_time += deltaT