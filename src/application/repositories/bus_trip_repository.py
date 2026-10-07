from abc import ABC, abstractmethod

class BusTripRepository(ABC):
    @abstractmethod
    def get_by_trip_number(self, trip_number: str):
        """Retrieve a bus trip by its trip number."""

    
    @abstractmethod
    def save(self, trip) -> None:  #returns none for a misssing trip and raises InvalidBooking
        """Store or update a bus trip"""