from datetime import datetime

from src.application.DTOs.booking_request import BookingRequest
from src.application.services.booking_application_service import (
    BookingApplicationService,
)
from src.infrastructure.in_memory_bus_trip_repository import (
    InMemoryBusTripRepository,
)
from src.infrastructure.in_memory_booking_repository import (
    InMemoryBookingRepository,
)
from src.domain.entities.bus_trip import BusTrip
from src.domain.exceptions import DomainError


def make_booking(service):
    """Ask for one booking's details, send it to the application layer, show the result."""
    print("\n--- Make a Booking ---")

    passenger_name = input("Enter passenger name: ").strip()
    trip_number = input("Enter trip number: ").strip()

    try:
        seat_number = int(input("Enter seat number: "))

        request = BookingRequest(
            passenger_name=passenger_name,
            trip_number=trip_number,
            seat_number=seat_number,
        )

        print("\nProcessing booking...")
        response = service.book_seat(request)

        print("\n" + "=" * 45)
        print("       BOOKING RESULT")
        print("=" * 45)
        print(f"Booking ID : {response.booking_id}")
        print(f"Passenger  : {response.passenger}")
        print(f"Trip       : {response.trip_number}")
        print(f"Seat       : {response.seat_number}")
        print(f"Status     : {response.status}")
        print("=" * 45)

    except ValueError:
        print("\nBooking failed: Seat number must be a whole number.")

    except DomainError as e:
        print(f"\nBooking failed: {e}")


def main():
    # Create the infrastructure dependencies ONCE, so they remember
    # every booking made while the program is running.
    trips = InMemoryBusTripRepository()
    bookings = InMemoryBookingRepository()

    # Create the application service and inject the repositories.
    service = BookingApplicationService(trips, bookings)

    # Add an available trip to the system.
    trips.save(
        BusTrip(
            "T001",
            datetime(2026, 10, 2, 8, 0),
            capacity=40,
        ),
    )

    trips.save(
        BusTrip(
            "T002",
            datetime(2026, 10, 5, 10, 0),
            capacity=30,
        ),
    )

    trips.save(

        BusTrip(
            "T003",
            datetime(2026, 10, 10, 9, 0),
            capacity=45,
        ),


    )

    print("=" * 45)
    print("       BUS TRIP BOOKING SYSTEM")
    print("=" * 45)

    print("\nAvailable trips:")
    print("Trip number: T001")
    print("Departure: 2 October 2026 at 08:00")
    print("Capacity: 40 seats")

    print()

    print("Trip number: T002")
    print("Departure: 5 October 2026 at 10:00")
    print("Capacity: 30 seats")

    print()

    print("Trip number: T003")
    print("Departure: 10 October 2026 at 9:00")
    print("Capacity: 45 seats")



    # The loop keeps the same repositories alive between bookings.
    while True:
        make_booking(service)

        again = input("\nMake another booking? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Bus Trip Booking System.")
            break


if __name__ == "__main__":
    main()