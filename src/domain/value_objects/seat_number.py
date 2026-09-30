
class SeatNumber:
    def __init__(self, number: int, capacity: int):
        if number <= 0:
            raise ValueError("Seat number must be positive")

        if number > capacity:
            raise ValueError("Seat number cannot exceed bus capacity")

        self.value = number 


