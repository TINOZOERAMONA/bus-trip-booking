#t1

import pytest
from src.domain.exceptions import InvalidSeatNumber
from src.domain.value_objects.seat_number import SeatNumber


def test_T1_seat_number_must_be_a_positive_whole_number():
    
    # boundary case: smallest valid seat
    assert SeatNumber(1).value == 1

    # rejection cases
    with pytest.raises(InvalidSeatNumber):
        SeatNumber(0)            
    with pytest.raises(InvalidSeatNumber):
        SeatNumber(-5)           # negative
    with pytest.raises(InvalidSeatNumber):
        SeatNumber(2.5)          # not a whole number

    # value equality: no separate identity
    assert SeatNumber(12) == SeatNumber(12)