from enum import Enum

from src.domain.base import AggregateRoot
from src.domain.events import BookingCreated
from src.domain.exceptions import InvalidBooking
from src.domain.value_objects.seat_number import SeatNumber


class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"


class Booking(AggregateRoot):
    

    def __init__(self, booking_id: str, passenger: str, trip_number: str,
                 seat: SeatNumber, status: BookingStatus = BookingStatus.PENDING):
        super().__init__()
        if not booking_id or not booking_id.strip():
            raise InvalidBooking("Booking needs an id")
        if not passenger or not passenger.strip():
            raise InvalidBooking("Booking needs a passenger")
        if not trip_number:
            raise InvalidBooking("Booking needs a trip")
        if not isinstance(seat, SeatNumber):
            raise InvalidBooking("Booking needs a valid seat")
        self._booking_id = booking_id
        self._passenger = passenger
        self._trip_number = trip_number
        self._seat = seat
        self._status = status

    @classmethod
    def create(cls, booking_id, passenger, trip_number, seat) -> "Booking":
        booking = cls(booking_id, passenger, trip_number, seat)
        booking._record(BookingCreated(booking_id, trip_number, seat))   # BR5
        return booking

    @property
    def booking_id(self): return self._booking_id
    @property
    def passenger(self): return self._passenger
    @property
    def trip_number(self): return self._trip_number
    @property
    def seat(self): return self._seat
    @property
    def status(self): return self._status

    def confirm(self):
        self._require_pending()
        self._status = BookingStatus.CONFIRMED

    def reject(self):
        self._require_pending()
        self._status = BookingStatus.REJECTED

    def _require_pending(self):
        if self._status is not BookingStatus.PENDING:
            raise InvalidBooking("Only a pending booking can change status")

    def __eq__(self, other):
        return isinstance(other, Booking) and other._booking_id == self._booking_id

    def __hash__(self):
        return hash(self._booking_id)


