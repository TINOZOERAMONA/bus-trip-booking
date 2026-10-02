#DTO's job is to carry data from one part of the application to another.


from dataclasses import dataclass


@dataclass
class BookingResponse:
    booking_id: str
    passenger: str
    trip_number: str
    seat_number: int
    status: str 

