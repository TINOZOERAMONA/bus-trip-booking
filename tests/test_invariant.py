from datetime import datetime

import pytest

from src.domain.entities.bus_trip import BusTrip
from src.domain.exceptions import InvalidSeatNumber, SeatAlreadyAllocated
from src.domain.value_objects.seat_number import SeatNumber

DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_T3_trip_never_allocates_a_seat_twice_or_outside_its_capacity():
    """T3 / BR3: invariant protected by the BusTrip aggregate root."""
    trip = BusTrip("T001", DEPARTURE, capacity=40)

    # boundary case: the last valid seat (40) is accepted
    trip.allocate_seat(SeatNumber(40))
    assert SeatNumber(40) in trip.allocated_seats

    # rejection case 1: seat beyond capacity (41)
    with pytest.raises(InvalidSeatNumber):
        trip.allocate_seat(SeatNumber(41))

    # rejection case 2: same seat allocated twice
    trip.allocate_seat(SeatNumber(12))
    with pytest.raises(SeatAlreadyAllocated):
        trip.allocate_seat(SeatNumber(12))

    # rejected attempts leave the aggregate unchanged
    assert trip.allocated_seats == {SeatNumber(40), SeatNumber(12)}