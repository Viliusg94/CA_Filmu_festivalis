class Schedule:
    def __init__(self, movie, screening_date, screening_time, seats=10):
        self.movie = movie
        self.screening_date = screening_date
        self.screening_time = screening_time
        self.total_seats = seats
        self.available_seats = seats
        self.reservations = []
    
    def __repr__(self):
        return (f"Filmų tvarkaraštis:\n{self.movie.name}, Data - {self.screening_date}, Laikas - {self.screening_time}, Laisvos vietos {self.available_seats}")
