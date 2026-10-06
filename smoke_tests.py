from datetime import datetime

from src.domain.entities.bus_trip import BusTrip
from src.application.DTOs.booking_request import BookingRequest
from src.application.services.booking_application_service import BookingApplicationService
from src.infrastructure.in_memory_booking_repository import InMemoryBookingRepository
from src.infrastructure.in_memory_bus_trip_repository import InMemoryBusTripRepository
from src.domain.exceptions import InvalidBooking


# 1. Infrastructure: create the repositories
trips = InMemoryBusTripRepository()
bookings = InMemoryBookingRepository()

# 2. Put one trip in the "database"
trips.save(
    BusTrip(
        "T001",
        datetime(2026, 10, 2, 8, 0),
        capacity=40
    )
)

# 3. Dependency injection: give the repositories to the use case
use_case = BookingApplicationService(trips, bookings)


# 4. Happy path
try:
    response = use_case.book_seat(
        "B001",
        BookingRequest("John", "T001", 12)
    )
    print("B001:", response)

except Exception as e:
    print("B001 FAILED:", e)


# 5. Seat already taken
try:
    response = use_case.book_seat(
        "B002",
        BookingRequest("Mary", "T001", 12)
    )
    print("B002:", response)

except InvalidBooking as e:
    print("B002 correctly rejected:", e)


# 6. Invalid seat number — BR1
try:
    response = use_case.book_seat(
        "B003",
        BookingRequest("Sam", "T001", 0)
    )
    print("B003:", response)

except Exception as e:
    print("B003 correctly failed:", e)


# 7. Missing trip — BR6
try:
    response = use_case.book_seat(
        "B004",
        BookingRequest("Ann", "T999", 5)
    )
    print("B004:", response)

except InvalidBooking as e:
    print("B004 correctly failed:", e)