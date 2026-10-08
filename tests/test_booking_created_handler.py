#t5<DELETE THIS FILE>
from datetime import datetime

from src.domain.entities.bus_trip import BusTrip
from src.domain.events import BookingCreated
from src.domain.value_objects.seat_number import SeatNumber


DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_T7_booking_created_event_allocates_seat_on_bus_trip():
    """T7 / BR5: handling BookingCreated updates the BusTrip aggregate."""

    # This test will initially fail because the handler
    # does not exist yet.

    trip = BusTrip("T001", DEPARTURE, capacity=40)

    event = BookingCreated(
        booking_id="B001",
        trip_number="T001",
        seat=SeatNumber(5)
    )

    # Handler will be added after this test fails.
    from src.domain.handlers.booking_created_handler import BookingCreatedHandler

    handler = BookingCreatedHandler()

    handler.handle(event, trip)

    assert SeatNumber(5) in trip.allocated_seats