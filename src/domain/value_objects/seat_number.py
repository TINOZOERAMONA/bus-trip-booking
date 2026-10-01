

from dataclasses import dataclass

from src.domain.exceptions import InvalidSeatNumber


@dataclass(frozen=True)
class SeatNumber:
    """Value Object enforcing BR1: a seat number must be a positive whole number."""
    value: int

    def __post_init__(self):
        if isinstance(self.value, bool) or not isinstance(self.value, int):
            raise InvalidSeatNumber("Seat number must be a whole number")
        if self.value <= 0:
            raise InvalidSeatNumber("Seat number must be positive")

    def __str__(self):
        return str(self.value)