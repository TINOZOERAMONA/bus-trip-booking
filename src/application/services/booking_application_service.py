# application service It's basically the manager/coordinator
from src.application.repositories.bus_trip_repository import BusTripRepository
from src.application.repositories.booking_repository import BookingRepository

from src.application.DTOs.booking_request import BookingRequest
from src.application.DTOs.booking_response import BookingResponse

from src.domain.exceptions import InvalidBooking
from src.domain.services.seat_booking_service import SeatBookingService
from src.domain.aggregate.booking import Booking
from src.application.handlers.booking_created_handler import BookingCreatedHandler
from src.domain.value_objects.seat_number import SeatNumber


from src.domain.handlers.booking_created_handler import BookingCreatedHandler

class BookingApplicationService:
    """Application service that coordinates the booking use case."""

    def __init__(
        self,
        bus_trip_repository: BusTripRepository,  #making the service depend on the repositor instead of the domain model
        booking_repository: BookingRepository,
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
        self.booking_repository = booking_repository

    def book_seat(
        self,
        request: BookingRequest,
    ) -> BookingResponse:
        booking_id = self._generate_booking_id()

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
        
        booking.confirm()

        #persist both aggregates only after the handler succeeded
        self.booking_repository.save(booking)
        self.bus_trip_repository.save(trip)    

        # Convert the domain object into the output DTO.
        return BookingResponse(
            booking_id=booking.booking_id,
            passenger=booking.passenger,
            trip_number=booking.trip_number,
            seat_number=booking.seat.value,
            status=booking.status.value,
        )
    

    def _generate_booking_id(self):
        bookings = self.booking_repository.get_all()

        next_number = len(bookings) + 1

        return f"B{next_number:03d}"