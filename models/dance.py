from .generic_class import _GenericClass

class Dance(_GenericClass):
    
    def __init__(self, capacity, start_time):
        super().__init__(capacity, start_time)