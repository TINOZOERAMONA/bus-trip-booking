#t2

from datetime import datetime

import pytest

from src.domain.entities.bus_trip import BusTrip, TripStatus
from src.domain.exceptions import InvalidTrip
from src.domain.value_objects.seat_number import SeatNumber

DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_T2_bus_trip_is_identified_by_trip_number_even_when_state_changes():
    """T2 / BR2: identity is the trip number and survives state changes."""
    trip = BusTrip("T001", DEPARTURE, capacity=2)

    # same trip number = same entity, even if the object's state differs
    same_trip_other_copy = BusTrip("T001", DEPARTURE, capacity=2)
    other_trip = BusTrip("T002", DEPARTURE, capacity=2)
    assert trip == same_trip_other_copy
    assert trip != other_trip

    # state changes (OPEN -> FULL) but identity stays the same
    assert trip.status is TripStatus.OPEN
    trip.allocate_seat(SeatNumber(1))
    trip.allocate_seat(SeatNumber(2))
    assert trip.status is TripStatus.FULL
    assert trip.trip_number == "T001"
    assert trip == same_trip_other_copy

    # a trip without a trip number cannot exist
    with pytest.raises(InvalidTrip):
        BusTrip("", DEPARTURE, capacity=2)


