from dataclasses import dataclass

from src.domain.value_objects.seat_number import SeatNumber


@dataclass(frozen=True)
class BookingCreated:
    """BR5 domain event: something that already happened (past tense)."""
    booking_id: str
    trip_number: str
    seat: SeatNumber


    