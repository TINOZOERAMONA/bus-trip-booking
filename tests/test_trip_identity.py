


from src.domain.entities.bus_trip import BusTrip

def test_T2_trip_is_identified_by_trip_number():
    trip = BusTrip("T001", "Kampala", "Gulu", "2026-10-01 08:00", 40)

    assert trip.trip_number == "T001"