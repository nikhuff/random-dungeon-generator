class Room:
    def __init__(self):
        self.room_left = None
        self.room_top = None
        self.room_bottom = None
        self.room_right = None

    def add_left(self, room):
        self.room_left = room

    def add_top(self, room):
        self.room_top = room

    def add_right(self, room):
        self.room_right = room

    def add_bottom(self, room):
        self.room_bottom = room

    