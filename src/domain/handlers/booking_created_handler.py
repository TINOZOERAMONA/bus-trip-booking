class BookingCreatedHandler:
    """Handles the BookingCreated domain event."""

    def handle(self, event, trip):
        trip.allocate_seat(event.seat)