

class DomainError(Exception):
    """Base class for every business-rule violation."""


class InvalidSeatNumber(DomainError):          # BR1
    pass


class SeatAlreadyAllocated(DomainError):       # BR3
    pass


class TripClosed(DomainError):                 # trip is full / sold out
    pass


class InvalidBooking(DomainError):             # Booking aggregate invariant
    pass




class InvalidTrip(DomainError):                # BR2
    pass