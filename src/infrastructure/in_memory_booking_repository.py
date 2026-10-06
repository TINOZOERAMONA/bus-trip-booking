from src.application.repositories.booking_repository import BookingRepository

class InMemoryBookingRepository(BookingRepository):

    def __init__(self):
        self._bookings = {}  #booking_id > Booking

    def get_by_id(self, booking_id: str):
        return self._bookings.get(booking_id)

    def save(self, booking) -> None:
        self._bookings[booking.booking_id] = booking