from src.domain.repositories.bus_trip_repository import BusTripRepository


class InMemoryBusTripRepository(BusTripRepository):
    """In-memory implementation of the BusTrip repository."""

    def __init__(self):
        self._trips = {}

    def save(self, trip):
        self._trips[trip.trip_number] = trip

    def get_by_trip_number(self, trip_number: str):
        return self._trips.get(trip_number)