#this one says Any repository for BusTrip must provide a way to get a BusTrip using its trip number."
#then the inmemory is what retrieves

# It's the abstraction/contract that says retrieval by trip number must be available. It doesn't perform the retrieval itself.

from abc import ABC, abstractmethod


class BusTripRepository(ABC):
    """Repository abstraction for retrieving BusTrip aggregates."""

    @abstractmethod
    def get_by_trip_number(self, trip_number: str):
        """Retrieve a BusTrip by its trip number."""
        pass