class Booking:
    def __init__(self, username, timestamp, class_name):
        self._username = username
        self._timestamp = timestamp
        self._class_name = class_name
        self.status = "WAITING"
    
    def set_booked(self):
        self.status = "BOOKED"