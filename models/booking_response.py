class BookingResponse:
    def __init__(self, class_name, status):
        self.__class_name = class_name
        self.__status = status
        
    def get_class_name(self):
        return self.__class_name
    
    def get_status(self):
        return self.__status