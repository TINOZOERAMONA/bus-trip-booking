#This carries the input to the Book Seat use case.
#use case is book a seat 

from dataclasses import dataclass


@dataclass(frozen=True)
class BookingRequest:
    passenger_name: str
    trip_number: str
    seat_number: int
