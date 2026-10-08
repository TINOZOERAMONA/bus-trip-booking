#DTO's job is to carry data from one part of the application to another.


from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BookingResponse:
    booking_id: str
    passenger: str
    trip_number: str
    seat_number: int
    status: str 
    message: Optional[str] = None  # why it was rejected, if it was

