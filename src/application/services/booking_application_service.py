# application service It's basically the manager/coordinator



from src.application.DTOs.booking_request import BookingRequest
from src.application.DTOs.booking_response import BookingResponse

from src.domain.exceptions import InvalidBooking
from src.domain.services.seat_booking_service import SeatBookingService
from src.domain.aggregate.booking import Booking
from src.domain.handlers.booking_created_handler import BookingCreatedHandler
from src.domain.value_objects.seat_number import SeatNumber


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

    def book_seat(
        self,
        booking_id: str,
        request: BookingRequest,
    ) -> BookingResponse:

        # BR6: retrieve the selected trip by trip number.
        trip = self.bus_trip_repository.get_by_trip_number(
            request.trip_number
        )

        if trip is None:
            raise InvalidBooking(
                f"Bus trip {request.trip_number} does not exist"
            )

        # Convert the primitive value from the DTO
        # into the domain Value Object.
        seat = SeatNumber(request.seat_number)

        # BR4: check whether the selected seat is available.
        if not self.seat_booking_service.can_book(
            trip=trip,
            passenger=request.passenger_name,
            seat_number=seat,
        ):
            raise InvalidBooking(
                f"Seat {seat} is not available "
                f"on trip {request.trip_number}"
            )

        # Create the domain object.
        booking = Booking.create(
            booking_id=booking_id,
            passenger=request.passenger_name,
            trip_number=request.trip_number,
            seat=seat,
        )

        # BR5: handle the BookingCreated domain event.
        for event in booking.pull_events():
            self.booking_created_handler.handle(event, trip)

        # Convert the domain object into the output DTO.
        return BookingResponse(
            booking_id=booking.booking_id,
            passenger=booking.passenger,
            trip_number=booking.trip_number,
            seat_number=booking.seat.value,
            status=booking.status.value,
        )