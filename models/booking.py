class Booking:
    def __init__(self, username, timestamp, class_name, start_time):
        self._username = username
        self._timestamp = timestamp
        self._class_name = class_name
        self.status = "WAITING"
        self._start_time = start_time
    def set_booked(self):
        self.status = "BOOKED"