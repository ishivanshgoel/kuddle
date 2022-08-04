class _GenericClass:
    def __init__(self, capacity, start_time):
        self._capacity = capacity
        self._waiting_list = []
        self._start_time = start_time
        self._total_registrations = 0
    
    def get_capacity(self):
        return self._capacity

    def get_total_registration(self):
        return self._total_registrations

    def add_registartion(self):
        self._total_registrations += 1
    
    def add_to_waiting(self, username):
        self._waiting_list.append(username)
    
    def remove_registartion(self):
        if self._total_registrations > 0:
            self._total_registrations -= 1
            
            if len(self._waiting_list) > 0:
                username = self._waiting_list[0]
                self._waiting_list.pop(0)
                return username
    
    def get_start_time(self):
        return self.start_time