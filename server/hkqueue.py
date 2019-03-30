class HkQueue():
    avg_examination_time = 12
    start_time = 8 * 60
    end_time = 16 * 60
    
    def __init__(self):
        self.slot_available = True
        self.timeline = []
    
    def get_first_free_slot(self):
        pass

    def add_patient(self, patient):
        self.timeline.append(patient)
        self.timeline.sort(key = lambda p: p.appointment_time)
    
    def offset_appointments(self, deltaT):
        pass

    def get_patients_in_queue(self):
        return len(self.timeline)

    def remove_patient(self):
        self.timeline.pop(0)