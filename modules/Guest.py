class Guest:
    def __init__(self, name):
        self.name = name
        self.reservations = []

    def __repr__(self):
        return (f"Žiūrovas: {self.name}")