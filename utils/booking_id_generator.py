class BookingIdGeneator:
    def __init__(self):
        self.id = 0
    
    def newId(self):
        self.id += 1
        return id