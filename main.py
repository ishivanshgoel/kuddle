from services import booking_service
from services import user_service

try:
    us = user_service.UserService()
    bs = booking_service.BookingService(user_service = us)
except Exception as ex:
    print(ex)

try:
    for i in range(100):
        us.register(f"shivansh-{i}")
    
    for i in range(100):
        bs.book_new_class("yoga", f"shivansh-{i}")
    
    bookings = bs.get_bookings()
    
    for booking in bookings.values():
        print(booking.status)
    
    print(bs.cancel_class("shivansh-0"))
    
except Exception as ex:
    print(ex)