from datetime import datetime

import pytest

from src.domain.entities.bus_trip import BusTrip
from src.domain.events import BookingCreated
from src.domain.exceptions import SeatAlreadyAllocated
from src.domain.handlers.booking_created_handler import BookingCreatedHandler
from src.domain.value_objects.seat_number import SeatNumber


DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_T8_handler_rejects_booking_created_for_already_allocated_seat():
    """T8: BusTrip rejects the event follow-up when the seat is already allocated."""

    # GIVEN:
    # The trip already has seat 5 allocated.
    trip = BusTrip("T001", DEPARTURE, capacity=40)
    seat = SeatNumber(5)

    trip.allocate_seat(seat)

    event = BookingCreated(
        booking_id="B002",
        trip_number="T001",
        seat=seat
    )

    handler = BookingCreatedHandler()

    # WHEN / THEN:
    # The handler asks BusTrip to allocate seat 5 again.
    # The aggregate must reject the operation.
    with pytest.raises(SeatAlreadyAllocated):
        handler.handle(event, trip)

    # The final state must still contain seat 5 only once.
    assert trip.allocated_seats == {seat}