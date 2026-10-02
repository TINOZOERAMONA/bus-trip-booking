#t4

from datetime import datetime

from src.domain.entities.bus_trip import BusTrip
from src.domain.services.seat_booking_service import SeatBookingService
from src.domain.value_objects.seat_number import SeatNumber


DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_T4_booking_is_allowed_when_seat_is_available():
    """T4 / BR4: booking is allowed when the selected seat is free."""

    # GIVEN:
    # A bus trip with capacity 40.
    trip = BusTrip("T001", DEPARTURE, capacity=40)

    # Seat 5 has not been allocated yet.
    seat = SeatNumber(5)

    # WHEN:
    service = SeatBookingService()

    result = service.can_book(
        trip=trip,
        passenger="Passenger 1",
        seat_number=seat
    )

    # THEN:
    assert result is True


def test_T4_booking_is_rejected_when_seat_is_unavailable():
    """T4 / BR4: booking is rejected when the selected seat is not free."""

    # GIVEN:
    trip = BusTrip("T001", DEPARTURE, capacity=40)

    # Seat 5 has already been allocated.
    seat = SeatNumber(5)
    trip.allocate_seat(seat)

    # WHEN:
    service = SeatBookingService()

    result = service.can_book(
        trip=trip,
        passenger="Passenger 1",
        seat_number=seat
    )

    # THEN:
    assert result is False