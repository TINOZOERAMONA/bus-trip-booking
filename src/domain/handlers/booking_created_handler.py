from src.domain.events import BookingCreated


class BookingCreatedHandler:
    """Handles a BookingCreated event by allocating the seat on the trip."""

    def handle(self, event: BookingCreated, trip):
        trip.allocate_seat(event.seat)