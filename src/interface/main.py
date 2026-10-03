from src.application.services.booking_application_service import BookingApplicationService
from src.infrastructure.in_memory_bus_trip_repository import InMemoryBusTripRepository
from src.infrastructure.in_memory_booking_repository import InMemoryBookingRepository

def build_service():
    trips = InMemoryBusTripRepository()
    bookings = InMemoryBookingRepository()
    return BookingApplicationService(trips, bookings), trips, bookings