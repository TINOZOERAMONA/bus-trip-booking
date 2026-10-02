#t6

from datetime import datetime

import pytest

from src.application.DTOs.booking_request import BookingRequest

from src.domain.entities.bus_trip import BusTrip
from src.domain.exceptions import InvalidBooking
#from src.domain.value_objects.seat_number import SeatNumber
from src.infrastructure.repositories.in_memory_bus_trip_repository import (
    InMemoryBusTripRepository,
)
from src.application.services.booking_application_service import (
    BookingApplicationService,
)


DEPARTURE = datetime(2026, 10, 2, 8, 0)

#tests if trip can be retrieved
def test_T6_bus_trip_can_be_retrieved_by_trip_number():
    """T6 / BR6: BusTrip is retrieved from the repository by trip number."""
    trip = BusTrip("T001", DEPARTURE, capacity=40)

    repository = InMemoryBusTripRepository()
    repository.save(trip)

    result = repository.get_by_trip_number("T001")

    assert result is trip
    assert result.trip_number == "T001"


#tests if Unknown trip returns None 
def test_T6_returns_none_when_bus_trip_does_not_exist():
    """T6 / BR6: repository returns None for an unknown trip number."""
    repository = InMemoryBusTripRepository()

    result = repository.get_by_trip_number("T999")

    assert result is None


#tests if Application Service rejects booking for missing trip.
# def test_T6_application_service_rejects_booking_for_missing_trip():
#     """T6 / BR6: booking is rejected when the selected trip does not exist."""
#     repository = InMemoryBusTripRepository()
#     service = BookingApplicationService(repository)

#     with pytest.raises(InvalidBooking):
#         service.book_seat(
#             booking_id="B001",
#             passenger="Passenger 1",
#             trip_number="T999",
#             seat=SeatNumber(5),
#         )



def test_T6_application_service_rejects_booking_for_missing_trip():
    """T6 / BR6: booking is rejected when the selected trip does not exist."""
    repository = InMemoryBusTripRepository()
    service = BookingApplicationService(repository)

    request = BookingRequest(
        passenger_name="Passenger 1",
        trip_number="T999",
        seat_number=5,
    )

    with pytest.raises(InvalidBooking):
        service.book_seat(
            booking_id="B001",
            request=request,
        )