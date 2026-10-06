
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
from src.domain.exceptions import InvalidBooking


def main():
    # Create the infrastructure dependencies.
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
        )
    )

    print("=" * 45)
    print("       BUS TRIP BOOKING SYSTEM")
    print("=" * 45)

    print("\nAvailable trip:")
    print("Trip number: T001")
    print("Departure: 2 October 2026 at 08:00")
    print("Capacity: 40 seats")

    print("\n--- Make a Booking ---")

    # Get booking information from the user.
    booking_id = input("Enter booking ID: ").strip()
    passenger_name = input("Enter passenger name: ").strip()
    trip_number = input("Enter trip number: ").strip()

    try:
        seat_number = int(input("Enter seat number: "))

        # Create the input DTO.
        request = BookingRequest(
            passenger_name=passenger_name,
            trip_number=trip_number,
            seat_number=seat_number,
        )

        print("\nProcessing booking...")

        # Send the request to the application layer.
        response = service.book_seat(
            booking_id=booking_id,
            request=request,
        )

        # Display the output DTO returned by the application layer.
        print("\n" + "=" * 45)
        print("       BOOKING SUCCESSFUL")
        print("=" * 45)
        print(f"Booking ID : {response.booking_id}")
        print(f"Passenger  : {response.passenger}")
        print(f"Trip       : {response.trip_number}")
        print(f"Seat       : {response.seat_number}")
        print(f"Status     : {response.status}")
        print("=" * 45)

    except ValueError:
        print("\nBooking failed: Seat number must be a whole number.")

    except InvalidBooking as e:
        print(f"\nBooking failed: {e}")


if __name__ == "__main__":
    main()

