class _GenericClass:
    def __init__(self, capacity, start_time):
        self._capacity = capacity
        self._waiting_list = []
        self.start_time = start_time
        self._total_registrations = 0
    
    def get_capacity(self):
        return self._capacity

    def get_total_registration(self):
        return self._total_registrations

    def add_registartion(self):
        self._total_registrations += 1
    
    def remove_registartion(self):
        self._total_registrations -= 1
    
    def add_to_waiting(self, username):
        self._waiting_list.append(username)