class Seat:

    total_seat = 0

    def __init__(self, seat_number, is_reserved = False):
        self.seat_number = seat_number
        self.is_reserved = is_reserved
        Seat.total_seat += 1

    def reserve(self):
        if self.is_reserved:
            return "Seat already reserved"
        else:
            self.is_reserved = True
            return "Seat reserved successfully"

    @staticmethod
    def is_valid_seat_number(seat_number):
        if seat_number > 0 and type(seat_number) is int:
            return True
        else:
            return False

    @classmethod
    def get_total_seats(cls):
        return cls.total_seat
    