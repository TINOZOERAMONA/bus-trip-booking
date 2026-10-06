from datetime import datetime
from src.application.DTOs.booking_request import BookingRequest
from src.domain.entities.bus_trip import BusTrip
from src.domain.exceptions import InvalidBooking
from src.application.services.booking_application_service import BookingApplicationService
from src.infrastructure.in_memory_bus_trip_repository import InMemoryBusTripRepository
from src.infrastructure.in_memory_booking_repository import InMemoryBookingRepository

def main():
    #Infrastracture created here, outside the service, and passed in as a dependency
    trips = InMemoryBusTripRepository()
    bookings = InMemoryBookingRepository()
    service = BookingApplicationService(trips, bookings)

    trips.save(BusTrip("T001", datetime(2026, 10, 2, 8, 0), capacity=40))

    request = BookingRequest(
        passenger_name="John Doe",
        trip_number="T001",
        seat_number=5,
    )

    try:
        response = service.book_seat(booking_id = "B001", request=request)
        print(f"Booking successful: {response.booking_id}")
    except InvalidBooking as e:
        print(f"Booking failed: {e}")    

    try:
        response = service.book_seat(booking_id = "B002", request=request)
        print(f"Booking successful: {response.booking_id}")
    except InvalidBooking as e:
        print(f"Booking failed: {e}")
if __name__ == "__main__":
    main()