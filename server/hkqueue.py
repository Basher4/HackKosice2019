import email_sender

class HkQueue(object):
    avg_examination_time = 10
    start_time = 8 * 60
    end_time = 16 * 60
    
    def __init__(self):
        self.slot_available = True
        self.timeline = []
        self.end_index = 0
    
    def fix_timeline_overlaps(self): #fix_first_free_slot
        if self.end_index == len(self.timeline) - 1:
            if self.timeline[self.end_index].appointment_time + self.avg_examination_time + 1 < self.end_time:
                self.end_index += 1
                return False
            else:
                return True
        else:
            current_appointment_end = self.timeline[self.end_index].appointment_time + self.avg_examination_time
            next_appointment_start = self.timeline[self.end_index + 1].appointment_time
            if current_appointment_end <= next_appointment_start:
                self.end_index += 1
                return False
            else:
                self.timeline[self.end_index + 1].reschedule(current_appointment_end + 2) # maybe len +1
                self.end_index += 1
                self.fix_timeline_overlaps()
                return False

    def add_patient(self, patient):
        self.timeline.append(patient)
        
    def sort_timeline(self):
        self.timeline.sort(key = lambda p: (p.appointment_time, p.sn))

    def get_patients_in_queue(self):
        return len(self.timeline)

    def remove_patient(self):
        if len(self.timeline) > 0:
            self.timeline.pop(0)
