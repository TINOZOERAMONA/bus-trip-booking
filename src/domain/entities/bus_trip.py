
from datetime import datetime
from enum import Enum

from src.domain.base import AggregateRoot
from src.domain.exceptions import SeatAlreadyAllocated, TripClosed, InvalidSeatNumber, InvalidTrip
from src.domain.value_objects.seat_number import SeatNumber


class TripStatus(Enum):
    OPEN = "OPEN"
    FULL = "FULL"


class BusTrip(AggregateRoot):
    """Aggregate B / Aggregate Root. Identity = trip_number (BR2).
    Invariant (BR3): a seat can never be allocated twice within one trip."""

    def __init__(self, trip_number: str, departure_time: datetime, capacity: int):
        super().__init__()
        if not trip_number or not str(trip_number).strip():
            raise InvalidTrip("A trip must have a trip number")        # BR2
        if capacity <= 0:
            raise InvalidTrip("Capacity must be positive")
        self._trip_number = trip_number
        self._departure_time = departure_time
        self._capacity = capacity
        self._allocated: set[SeatNumber] = set()
        self._status = TripStatus.OPEN

    # identity
    @property
    def trip_number(self): return self._trip_number
    @property
    def capacity(self): return self._capacity
    @property
    def departure_time(self): return self._departure_time
    @property
    def status(self): return self._status
    @property
    def allocated_seats(self): return frozenset(self._allocated)   # read-only copy

    def is_open(self) -> bool:
        return self._status is TripStatus.OPEN

    def is_seat_free(self, seat: SeatNumber) -> bool:
        return seat not in self._allocated

    def allocate_seat(self, seat: SeatNumber) -> None:
        """The ONLY way to change the seat collection, so BR3 cannot be bypassed."""
        if not self.is_open():
            raise TripClosed(f"Trip {self._trip_number} is no longer accepting bookings")
        if seat.value > self._capacity:
            raise InvalidSeatNumber(f"Seat {seat} is outside capacity {self._capacity}")
        if seat in self._allocated:
            raise SeatAlreadyAllocated(
                f"Seat {seat} is already allocated on trip {self._trip_number}")
        self._allocated.add(seat)
        if len(self._allocated) == self._capacity:
            self._status = TripStatus.FULL                          # close when sold out

    def __eq__(self, other):                                        # entity: equal by identity
        return isinstance(other, BusTrip) and other._trip_number == self._trip_number

    def __hash__(self):
        return hash(self._trip_number)

