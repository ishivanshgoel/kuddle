from models.dance import Dance
from models.gym import Gym
from models.yoga import Yoga
from models.booking import Booking
from .user_service import UserService

class BookingService:
    def __init__(self, user_service):
        
        try:
            # to hold bookings data
            # key will be username
            # and value will be booking model
            # it is assumed that only one registration per user
            
            if isinstance(user_service, UserService) == False:
                raise TypeError("user_service should be an instance of UserService")
            
            # user_service for user level operations
            self.__user_service = user_service
            
            # to store booking data
            self.__bookings = {}
            
            self.__booking_id_counter = 1
            
            # dummy capacity values as 50 for each class
            self.__yoga_classes = Yoga(50, 150)
            self.__dance_classes = Dance(50, 160)
            self.__gym_classes = Gym(50, 130)
        except Exception as ex:
            raise ex
    
    def book_new_class(self, class_type, username):
        try:
            if self.__user_service.authenticate(username) == False:
                raise Exception("unauthorized user")
            if class_type == "yoga":
                return self.__register_in_yoga_class(username)
            elif class_type == "dance":
                return self.__register_in_dance_class(username)
            elif class_type == "gym":
                return self.__register_in_gym_class(username)
            else:
                raise Exception("class_type is invalid")
        except Exception as ex:
            raise ex
    
    def cancel_class(self, username):
        # allow cancellation only if it is cancelled before 30 minutes of class start time
        
        # dummy current time
        current_time = 140
        if username in self._bookings:
            if self.__bookings[username].start_time - current_time <= 30:
                return True
            else:
                return False
        else:
            return False
    
    def get_bookings(self):
        return self.__bookings
    
    def __register_in_yoga_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        yoga_classes = self.__yoga_classes
        capacity = yoga_classes.get_capacity()
        total_registrations = yoga_classes.get_total_registration()
        
        if(capacity <= total_registrations):
            yoga_classes.add_to_waiting(username)
        
        else:
            self.__yoga_classes.add_registartion()
            booking.set_booked()
        
        self.__bookings[username] = booking
        return booking
    
    def __register_in_dance_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        dance_classes = self.__dance_classes
        capacity = dance_classes.get_capacity()
        total_registrations = dance_classes.get_total_registration()
        
        if(capacity <= total_registrations):
            dance_classes.add_to_waiting(username)
        
        else:
            self.__yoga_classes.add_registartion()
            booking.set_booked()
        
        self.__bookings[username] = booking
        return booking

    def __register_in_gym_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        gym_classes = self.__gym_classes
        capacity = gym_classes.get_capacity()
        total_registrations = gym_classes.get_total_registration()
        
        if(capacity <= total_registrations):
            gym_classes.add_to_waiting(username)
        
        else:
            self.__gym_classes.add_registartion()
            booking.set_booked()
        
        self.__bookings[username] = booking
        return booking
    
    def _increment_booking_count(self):
        self.__booking_id_counter += 1
        