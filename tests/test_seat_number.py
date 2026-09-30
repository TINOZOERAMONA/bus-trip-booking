#TI which is the test for seat number 

from src.domain.value_objects.seat_number import SeatNumber


def test_T1_seat_number_must_be_positive():
    try:
        SeatNumber(-1, 40)    #try to create seat number 0 on a bus with 40 seats rule says seat number must be positive
        assert False
    except ValueError:
        assert True