class HkQueue(object):
    avg_examination_time = 12
    start_time = 23 * 60
    end_time = 25 * 60
    
    def __init__(self):
        self.slot_available = True
        self.timeline = []
        self.end_index = 0
    
    def get_first_free_slot(self): #fix_first_free_slot
        if self.end_index == len(self.timeline) - 1:
            if self.timeline[self.end_index].appointment_time + self.avg_examination_time + 1 < self.end_time:
                self.end_index += 1
                return False
            else:
                return True
        else:
            if self.timeline[self.end_index].appointment_time + self.avg_examination_time <= self.timeline[self.end_index + 1].appointment_time:
                self.end_index += 1
                return False
            else:
                self.timeline[self.end_index + 1].appointment_time = self.timeline[self.end_index].appointment_time + self.avg_examination_time + 2 # maybe len +1
                self.end_index += 2
                self.get_first_free_slot()
                return False

    def add_patient(self, patient):
        self.timeline.append(patient)
        self.timeline.sort(key = lambda p: p.appointment_time)

    def get_patients_in_queue(self):
        return len(self.timeline)

    def remove_patient(self):
        if len(self.timeline) > 0:
            self.timeline.pop(0)
