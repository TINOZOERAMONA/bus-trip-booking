# #t7

# from datetime import datetime

# from src.application.services.booking_application_service import (
#     BookingApplicationService,
# )
# from src.domain.aggregate.booking import BookingStatus
# from src.domain.entities.bus_trip import BusTrip
# from src.domain.value_objects.seat_number import SeatNumber
# from src.infrastructure.repositories.in_memory_bus_trip_repository import (
#     InMemoryBusTripRepository,
# )


# DEPARTURE = datetime(2026, 10, 2, 8, 0)


# def test_booking_application_service_completes_booking_and_allocates_seat():
#     """BR6 + BR4 + BR5: successful booking completes the full use case."""
#     trip = BusTrip("T001", DEPARTURE, capacity=40)

#     repository = InMemoryBusTripRepository()
#     repository.save(trip)

#     service = BookingApplicationService(repository)

#     booking = service.book_seat(
#         booking_id="B001",
#         passenger="Passenger 1",
#         trip_number="T001",
#         seat=SeatNumber(5),
#     )

#     assert booking.booking_id == "B001"
#     assert booking.status is BookingStatus.PENDING
#     assert SeatNumber(5) in trip.allocated_seats




from datetime import datetime

from src.application.DTOs.booking_request import BookingRequest
from src.application.services.booking_application_service import (
    BookingApplicationService,
)
from src.domain.aggregate.booking import BookingStatus
from src.domain.entities.bus_trip import BusTrip
from src.domain.value_objects.seat_number import SeatNumber
from src.infrastructure.in_memory_bus_trip_repository import (
    InMemoryBusTripRepository,
)
from src.infrastructure.in_memory_booking_repository import InMemoryBookingRepository


DEPARTURE = datetime(2026, 10, 2, 8, 0)


def test_booking_application_service_completes_booking_and_allocates_seat():
    """BR6 + BR4 + BR5: successful booking completes the full use case."""

    trip = BusTrip("T001", DEPARTURE, capacity=40)

    repository = InMemoryBusTripRepository()
    repository.save(trip)

    booking_repository = InMemoryBookingRepository()

    service = BookingApplicationService(repository, booking_repository)

    request = BookingRequest(
        passenger_name="Passenger 1",
        trip_number="T001",
        seat_number=5,
    )

    response = service.book_seat(
        booking_id="B001",
        request=request,
    )

    # Verify the output DTO.
    assert response.booking_id == "B001"
    assert booking_repository.get_by_id("B001") is not None
    assert response.passenger == "Passenger 1"
    assert response.trip_number == "T001"
    assert response.seat_number == 5
    assert response.status == BookingStatus.PENDING.value

    # Verify BR5: the event was handled and Aggregate B changed.
    assert SeatNumber(5) in trip.allocated_seats