from abc import ABC, abstractmethod

class BookingRepository(ABC):
    @abstractmethod
    def get_by_id(self, booking_id: str):
        """Retrieve a booking by its booking ID."""

    @abstractmethod
    def save(self, booking) -> None:
        """Store or update a booking"""