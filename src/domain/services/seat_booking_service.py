# #A passenger can book a bus trip only if the selected trip has an available seat.

class SeatBookingService:

    #method takes the selected bustrip, passenger, and the seat they want 
    def can_book(self, trip, passenger, seat_number):
        #asks if a particular seat is available, we are accessing the is_seat_available function through trip
        #return trip.is_seat_free(seat_number)

        return (
            trip.is_open()
            and trip.is_seat_free(seat_number)
        )
    



# TDD RED phase - implementation temporarily removed