#application service It's basically the manager/coordinator


from src.domain.exceptions import InvalidBooking
from src.domain.services.seat_booking_service import SeatBookingService
from src.domain.aggregate.booking import Booking
from src.domain.handlers.booking_created_handler import BookingCreatedHandler


class BookingApplicationService:
    """Application service that coordinates the booking use case."""

    def __init__(
        self,
        bus_trip_repository,
        seat_booking_service=None,
        booking_created_handler=None,
    ):
        self.bus_trip_repository = bus_trip_repository
        self.seat_booking_service = (
            seat_booking_service or SeatBookingService()
        )
        self.booking_created_handler = (
            booking_created_handler or BookingCreatedHandler()
        )

    def book_seat(self, booking_id, passenger, trip_number, seat):
        # BR6: retrieve the selected trip by trip number
        trip = self.bus_trip_repository.get_by_trip_number(trip_number)

        if trip is None:
            raise InvalidBooking(
                f"Bus trip {trip_number} does not exist"
            )

        # BR4: check whether the selected seat is available
        if not self.seat_booking_service.can_book(
            trip=trip,
            passenger=passenger,
            seat_number=seat
        ):
            raise InvalidBooking(
                f"Seat {seat} is not available on trip {trip_number}"
            )

        # Create the booking.
        booking = Booking.create(
            booking_id=booking_id,
            passenger=passenger,
            trip_number=trip_number,
            seat=seat
        )

        # BR5: handle the BookingCreated event.
        for event in booking.pull_events():
            self.booking_created_handler.handle(event, trip)

        return booking