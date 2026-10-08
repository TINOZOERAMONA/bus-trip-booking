

class DomainError(Exception):
    """Base class for every business-rule violation."""


class InvalidSeatNumber(DomainError):          #represents violation of BR1
    pass


class TripClosed(DomainError):                 # trip is full / sold out BR2
    pass



class SeatAlreadyAllocated(DomainError):       # BR3 a seat can be allocated only once

    pass


class SeatOutOfRange(DomainError):         # BR3: seat is beyond the bus capacity
    pass


class BookingNotAllowed(DomainError):      # BR4: trip not open, or passenger already booked
    pass

class InvalidBooking(DomainError):             # Booking aggregate invariant
    pass



class InvalidTrip(DomainError):                # BR2  BusTrip construction invariant
    pass