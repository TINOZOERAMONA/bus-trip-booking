#t5

from src.domain.aggregate.booking import Booking
from src.domain.events import BookingCreated
from src.domain.value_objects.seat_number import SeatNumber


def test_T5_successful_booking_records_booking_created_event():
    """T5 / BR5: successful booking creation records BookingCreated."""

    # GIVEN:
    # A valid booking can be created.
    booking = Booking.create(
        booking_id="B001",
        passenger="Passenger 1",
        trip_number="T001",
        seat=SeatNumber(5)
    )

    # WHEN:
    # The application/domain layer pulls the events
    # recorded by the Booking aggregate.
    events = booking.pull_events()

    # THEN:
    # Exactly one BookingCreated event should have been recorded.
    assert len(events) == 1

    event = events[0]

    assert isinstance(event, BookingCreated)
    assert event.booking_id == "B001"
    assert event.trip_number == "T001"
    assert event.seat == SeatNumber(5)